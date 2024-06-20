# Receipt Generation Script

This Python script creates a payment receipt in PDF format. It includes details like transaction ID, date, buyer's name and contact information, items purchased, total amount, and payment method.

## Requirements

- Python 3.x
- ReportLab library

## Installation

1. **Install Python 3**: Download and install Python from [python.org](https://www.python.org/).

2. **Install ReportLab**: Open your terminal and run:

    ```
    pip install reportlab
    ```

## Usage

1. **Download the Script**: Save the script file to your computer.

2. **Modify the Script**: Update the example usage section in the script with your transaction details, items purchased, total amount, payment method, and buyer details.

3. **Run the Script**: In your terminal, navigate to the directory where the script is saved and run:

    ```sh
    python payment_receipt.py
    ```

This will create a PDF file named `receipt.pdf` in the same directory.

## Customization

Feel free to modify the script to fit your needs. You can change the layout, fonts, and positions of the text elements as required.

## Example Usage

You will need to provide the following details in the script:

- **Transaction ID**
- **Date**
- **Items Purchased**: List of items with names and prices
- **Total Amount**
- **Payment Method**
- **Buyer Details**: Name, address, and contact information
- **Filename**: Name of the output PDF file

## License

This project is licensed under the MIT License.
