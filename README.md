# African-Gates-Tours-Inventory-System
<!DOCTYPE html>
<html>
<head>
    <title>Adventure Tours Invoice</title>
    <style>
        /* Basic Styling - Customize as needed */
        body {
            font-family: sans-serif;
        }

        .invoice-header {
            text-align: center;
            margin-bottom: 20px;
        }

        .invoice-details {
            margin-bottom: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        .total {
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div class="invoice-header">
        <h1>Adventure Tours</h1>
        <p>Address: [Your Company Address]</p>
        <p>Phone: [Your Company Phone]</p>
        <p>Email: [Your Company Email]</p>
    </div>

    <div class="invoice-details">
        <p>Invoice Number: {{ invoice.invoice_number }}</p>
        <p>Invoice Date: {{ invoice.invoice_date }}</p>
        <p>Customer: {{ invoice.customer_name }}</p>
        <p>Address: {{ invoice.customer_address }}</p>
    </div>

    <table>
        <thead>
            <tr>
                <th>Item</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            {% for item in invoice.items %}
            <tr>
                <td>{{ item.name }}</td>
                <td>{{ item.quantity }}</td>
                <td>{{ item.price }}</td>
                <td>{{ item.quantity * item.price }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <div class="total">
        <p>Subtotal: {{ invoice.items | sum(attribute='quantity * price') }}</p>
        <p>Tax (if applicable): [Add tax calculation here]</p>
        <p>Total: [Add total calculation here]</p>
    </div>

</body>
</html>
