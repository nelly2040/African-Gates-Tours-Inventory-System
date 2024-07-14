from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
            'availability': self.availability.isoformat() if self.availability else None,
            'tour_type': self.tour_type
        }

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    email = db.Column(db.String(255))

class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.tour_id'), nullable=False)
    booking_date = db.Column(db.Date, default=date.today)
    num_people = db.Column(db.Integer)

    customer = db.relationship('Customer', backref='bookings')
    tour = db.relationship('Tour', backref='bookings')
