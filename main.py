from fpdf import FPDF
import re
import requests
from requests.auth import HTTPBasicAuth
import uuid
from datetime import datetime, timedelta
from typing import Type
import hmrc_funcs


class InvoiceSender:
    def __init__(
        self,
        name="",
        address_line1="",
        address_line2="",
        address_line3="",
        postcode="",
        vat_number="",
        company_number="",
        phone="",
        email="",
    ):
        self.name = name
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.address_line3 = address_line3
        self.postcode = postcode
        self.vat_number = vat_number
        self.company_number = company_number
        self.phone = phone
        self.email = email


class InvoiceRecipient:
    def __init__(
        self,
        name="",
        address_line1="",
        address_line2="",
        address_line3="",
        postcode="",
        vat_number="",
        company_number="",
        phone="",
        email="",
    ):
        self.name = name
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.address_line3 = address_line3
        self.postcode = postcode
        self.vat_number = vat_number
        self.company_number = company_number
        self.phone = phone
        self.email = email


class InvoiceDetails:
    def __init__(self, number=None, date=None, due_date=None):
        self.number = (
            number if number else str(uuid.uuid4())[:4]
        )  # Using the first 8 characters of a UUID

        # Check if a date is provided
        if date:
            # Convert the provided date from dd/MM/yyyy to a datetime object
            invoice_date = datetime.strptime(date, "%d/%m/%Y")
        else:
            # If no date is provided, set it to today's date
            invoice_date = datetime.now()

        self.date = invoice_date.strftime("%d/%m/%Y")

        # If no due_date is provided, set it to 14 days from the date
        if not due_date:
            due_date_obj = invoice_date + timedelta(days=14)
            self.due_date = due_date_obj.strftime("%d/%m/%Y")
        else:
            self.due_date = due_date


class InvoiceItem:
    def __init__(self, description="", quantity="", unit_price="", tax_percentage=0):
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
        self.tax_percentage = tax_percentage
        self.calculate_total()  # Calculate the total when the item is created

    def calculate_total(self):
        # Calculate the total including tax based on the tax_percentage
        self.total = (float(self.quantity) * float(self.unit_price)) * (
            1 + (self.tax_percentage / 100)
        )


class InvoiceData:
    def __init__(
        self,
        sender=InvoiceSender(),
        recipient=InvoiceRecipient(),
        details=InvoiceDetails(),
        items=[],
    ):
        self.sender = sender
        self.recipient = recipient
        self.details = details
        self.items = items


class PDF(FPDF):
    def header(self):
        # Logo (you can replace 'logo_demo.png' with your company's logo)
        self.image("channels4_profile.jpg", (self.w * 0.75), 8, 33)
        self.set_font("Arial", "B", 25)

        # Move to the right for the title
        self.cell(35.5, 10, "INVOICE", 0, 1, "C")
        self.ln(5)


def generate_invoice_adjusted(invoice_data):
    # Extracting data from the InvoiceData instance
    sender_info: Type[InvoiceSender] = invoice_data.sender
    recipient_data = invoice_data.recipient
    invoice_details = invoice_data.details
    items = invoice_data.items

    pdf = PDF()
    pdf.add_page()

    pdf.set_font("Arial", "", 12)

    verification_result = hmrc_funcs.verify_company_details(
        recipient_data.company_number,
        recipient_data.name,
        recipient_data.address_line1,
        recipient_data.postcode,
    )

    name_display = recipient_data.name
    address_display = recipient_data.address_line1
    postcode_display = recipient_data.postcode

    pdf.cell(0, 10, "To:", 0, 1)
    pdf.set_font("Arial", "B", 12)

    if verification_result.get("name_verified", False):
        pdf.set_text_color(0, 128, 0)  # Green
    else:
        pdf.set_text_color(255, 0, 0)  # Red

    pdf.cell(0, 6, name_display, 0, 1)
    pdf.set_font("Arial", "", 12)

    if verification_result.get("address_verified", False):
        pdf.set_text_color(0, 128, 0)  # Green
    else:
        pdf.set_text_color(255, 0, 0)  # Red

    pdf.cell(0, 6, address_display, 0, 1)

    pdf.set_text_color(0, 0, 0)

    if recipient_data.address_line2:  # Check if address line 2 is provided
        pdf.cell(0, 6, recipient_data.address_line2, 0, 1)

    pdf.cell(0, 6, f"{recipient_data.address_line3}", 0, 1)

    if verification_result.get("postcode_verified", False):
        pdf.set_text_color(0, 128, 0)  # Green
    else:
        pdf.set_text_color(255, 0, 0)  # Red

    pdf.cell(0, 6, f"{postcode_display}", 0, 1)

    pdf.ln(5)

    verification_result_vat = hmrc_funcs.verify_vat_number(recipient_data.vat_number)

    if (
        verification_result_vat["vat_verified"]
        and verification_result_vat["official_name"] == recipient_data.name
    ):
        pdf.set_text_color(0, 128, 0)  # Green
        vat_display = f"VAT: {recipient_data.vat_number} *"
    else:
        pdf.set_text_color(255, 0, 0)  # Red
        vat_display = f"VAT: {recipient_data.vat_number}"

    pdf.cell(0, 6, vat_display, 0, 1)

    pdf.set_text_color(0, 0, 0)

    if verification_result.get("name_verified", False):
        pdf.set_text_color(0, 128, 0)  # Green
    else:
        pdf.set_text_color(0, 0, 0)  # Default color (black)

    pdf.cell(0, 6, f"Company No: {recipient_data.company_number}", 0, 1)

    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, recipient_data.phone, 0, 1)
    pdf.cell(0, 6, recipient_data.email, 0, 1)
    pdf.ln(10)
    toXCoord = pdf.get_x()

    pdf.set_xy(145, 45)
    pdf.cell(0, 10, f"Invoice Number: {invoice_details.number}", 0, 1, "R")
    pdf.cell(0, 10, f"Date: {invoice_details.date}", 0, 1, "R")
    pdf.cell(0, 10, f"Due Date: {invoice_details.due_date}", 0, 1, "R")
    pdf.ln(10)

    pdf.set_x(toXCoord)
    pdf.ln(15)

    col_widths = [50, 50, 30, 30]
    pdf.set_fill_color(200, 220, 255)
    columns = ["Description", "Quantity", "Unit Price", "Total"]
    for i, column in enumerate(columns):
        pdf.cell(col_widths[i], 10, column, 1, 0, "C", 1)
    pdf.ln()

    total_amount = 0
    for item in items:
        # Use the tax_percentage from the InvoiceItem
        total = (
            float(item.quantity)
            * float(item.unit_price)
            * (1 + (item.tax_percentage / 100))
        )
        pdf.cell(col_widths[0], 10, item.description, 1)
        pdf.cell(col_widths[1], 10, str(item.quantity), 1)
        pdf.cell(col_widths[2], 10, f"£{float(item.unit_price):.2f}", 1)
        pdf.cell(col_widths[3], 10, f"£{total:.2f}", 1)
        pdf.ln()
        total_amount += total

    current_y = pdf.get_y() + 10

    # Calculate the total amount without any blanket tax percentage
    pdf.set_xy(pdf.get_x(), current_y)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(40, 10, "Total Amount:", 1, 0, "C", 1)
    pdf.cell(40, 10, f"£{total_amount:.2f}", 1, 1, "R")

    # Footer generation code here
    pdf.set_y((pdf.h) * 0.75)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "From:", 0, 1, "L")
    pdf.cell(0, 6, f"{sender_info.name}, {sender_info.address_line1}", 0, 1)
    pdf.cell(0, 6, f"Company No: {sender_info.company_number}", 0, 1)
    pdf.cell(0, 6, f"VAT No.: {sender_info.vat_number}", 0, 1)
    pdf.cell(0, 6, f"Phone: {sender_info.phone}, Email: {sender_info.email}", 0, 1)
    # pdf.set_y(-20)
    # pdf.set_font("Arial", "I", 8)
    # pdf.cell(0, 10, "Page " + str(pdf.page_no()), 0, 0, "C")

    file_name = f"invoice_adjusted_{invoice_details.number}.pdf"
    pdf.output(file_name)

    return file_name


# Sample data (you can change this to your actual data)
sender_data = InvoiceSender(
    name="Tech Co.",
    address_line1="123 Tech Street",
    address_line2="Tech City",
    address_line3="London",
    postcode="E1 1AA",
    company_number="01234567",
    vat_number="GB987654321",
    phone="020 1234 5678",
    email="techco@example.co.uk",
)

recipient_data = InvoiceRecipient(
    name="WILL TECHNOLOGY COMPAN LIMITED",
    address_line1="456 John Street",
    address_line2="John City",
    address_line3="London",
    postcode="E1 2AB",
    company_number="14249957",
    vat_number="GB123456789",
    phone="020 9876 5432",
    email="johndoe@example.co.uk",
)

invoice_details_data = InvoiceDetails(number="INV12345", date="06/10/2023")

items_data = [
    InvoiceItem(description="Laptop", quantity="1", unit_price="1000.00"),
    InvoiceItem(description="Mouse", quantity="2", unit_price="25.00"),
    InvoiceItem(description="Keyboard", quantity="1", unit_price="50.00"),
]

invoice_data_object = InvoiceData(
    sender=sender_data,
    recipient=recipient_data,
    details=invoice_details_data,
    items=items_data,
)

# To generate the invoice, call:
invoice_file = generate_invoice_adjusted(invoice_data_object)
print(invoice_file)
