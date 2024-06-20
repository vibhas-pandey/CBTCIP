from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_receipt(transaction_id, date, items, total_amount, payment_method, buyer_details, filename):
    # Create a canvas object
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Add the title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1 * inch, height - 1 * inch, "Payment Receipt")

    # Add transaction details
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.5 * inch, f"Transaction ID: {transaction_id}")
    c.drawString(1 * inch, height - 2 * inch, f"Date: {date}")

    # Add buyer details
    c.drawString(1 * inch, height - 2.5 * inch, f"Buyer Name: {buyer_details['name']}")
    c.drawString(1 * inch, height - 3 * inch, f"Address: {buyer_details['address']}")
    c.drawString(1 * inch, height - 3.5 * inch, f"Contact: {buyer_details['contact']}")

    # Add a line separator
    c.line(1 * inch, height - 3.7 * inch, 7.5 * inch, height - 3.7 * inch)

    # Add items
    y_position = height - 4.2 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1 * inch, y_position, "Items Purchased:")
    y_position -= 0.3 * inch

    c.setFont("Helvetica", 12)
    for item in items:
        c.drawString(1.2 * inch, y_position, f"{item['name']}: ${item['price']:.2f}")
        y_position -= 0.3 * inch

    # Add a line separator
    c.line(1 * inch, y_position - 0.2 * inch, 7.5 * inch, y_position - 0.2 * inch)

    # Add total amount
    y_position -= 0.5 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1 * inch, y_position, f"Total Amount: ${total_amount:.2f}")

    # Add payment method
    y_position -= 0.5 * inch
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, y_position, f"Payment Method: {payment_method}")

    # Save the PDF
    c.showPage()
    c.save()

# Example usage
transaction_id = "12345"
date = "2024-06-20"
items = [
    {"name": "Item 1", "price": 100.00},
    {"name": "Item 2", "price": 10.50},
    {"name": "Item 3", "price": 2.75}
]
total_amount = sum(item['price'] for item in items)
payment_method = "Credit Card"
buyer_details = {
    "name": "Gabbar Singh",
    "address": "12 Pahadi , Anytown, USA",
    "contact": "+1xx xxxx 000"
}
filename = "receipt.pdf"

create_receipt(transaction_id, date, items, total_amount, payment_method, buyer_details, filename)
