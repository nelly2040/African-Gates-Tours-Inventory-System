from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
# Get the database URI from the environment variable
database_uri = os.environ.get('DATABASE_URL')
# For SQLite (local development)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# For MySQL (production)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2040245800nm,.@localhost/african_gates_tours'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Tours (Simplified)
class Tour(db.Model):
    tour_id = db.Column(db.Integer, primary_key=True)
    tour_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    capacity = db.Column(db.Integer)
    availability = db.Column(db.Date)
    tour_type = db.Column(db.String(255))

    def to_dict(self):
        return {
            'tour_id': self.tour_id,
            'tour_name': self.tour_name,
            'description': self.description,
            'price': self.price,
            'capacity': self.capacity,
            'availability': self.availability.isoformat(),
            'tour_type': self.tour_type
        }

# Model for Customers (Simplified)
class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    email = db.Column(db.String(255))

# Model for Bookings (Simplified)
class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.tour_id'), nullable=False)
    booking_date = db.Column(db.Date, default=date.today)
    num_people = db.Column(db.Integer)
    customer = db.relationship('Customer', backref='bookings')
    tour = db.relationship('Tour', backref='bookings')

# Model for Equipment (Simplified)
class Equipment(db.Model):
    equipment_id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    condition = db.Column(db.String(255))
    rental_price = db.Column(db.Float)

# Model for Transportation (Simplified)
class Transportation(db.Model):
    vehicle_id = db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.String(255), nullable=False)
    capacity = db.Column(db.Integer)
    maintenance_schedule = db.Column(db.Date)
    insurance_info = db.Column(db.Text)
    availability = db.Column(db.Date)

# Model for Accommodation (Simplified)
class Accommodation(db.Model):
    accommodation_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    room_types = db.Column(db.String(255))
    rates = db.Column(db.Float)
    availability = db.Column(db.Date)
    contact_info = db.Column(db.Text)

# API Endpoints 
@app.route('/api/tours', methods=['GET'])
def get_tours():
    tours = Tour.query.all()
    return jsonify([tour.to_dict() for tour in tours])

@app.route('/api/tours/<int:tour_id>', methods=['GET'])
def get_tour(tour_id):
    tour = Tour.query.get_or_404(tour_id)
    return jsonify(tour.to_dict())

@app.route('/api/tours', methods=['POST'])
def create_tour():
    data = request.get_json()
    tour = Tour(
        tour_name=data['tour_name'],
        description=data.get('description'),
        price=data.get('price'),
        capacity=data.get('capacity'),
        availability=datetime.strptime(data['availability'], '%Y-%m-%d').date(),
        tour_type=data.get('tour_type')
    )
    db.session.add(tour)
    db.session.commit()
    return jsonify({'message': 'Tour created successfully'}), 201

@app.route('/api/book', methods=['POST'])
def book_tour():
    data = request.get_json()
    tour_id = data['tour_id']
    customer_name = data['customer_name']
    customer = Customer.query.filter_by(name=customer_name).first()
    if not customer:
        customer = Customer(name=customer_name)
        db.session.add(customer)
        db.session.commit()
    booking = Booking(
        customer_id=customer.customer_id,
        tour_id=tour_id,
        booking_date=date.today(),
        num_people=data['num_people']
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({'message': 'Booking successful'})

@app.route('/api/invoice/<int:booking_id>', methods=['GET'])
def generate_invoice(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    customer = booking.customer
    tour = booking.tour

    # Generate invoice data as a dictionary
    invoice_data = {
        'company_name': 'African Gates Tours',
        'invoice_number': booking.booking_id,
        'invoice_date': booking.booking_date.isoformat(),
        'customer_name': customer.name,
        'customer_address': customer.address,
        'items': [
            {'name': tour.tour_name, 'quantity': booking.num_people, 'price': tour.price}
        ]
        # ... (Add other invoice details)
    }

    # Render the invoice template
    return render_template('invoice.html', invoice=invoice_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
