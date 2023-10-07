# 🧾 SmartBillify

SmartBillify is a modest weekend project I've embarked on, aimed at generating PDF invoices with a touch of automation in Python.

## 🌟 Features

- **Generate PDF Invoices**: Simple and clean invoice design.
- **Companies House Lookup**: Verify company details in a jiffy.
- **VAT Verification**: Double-check VAT numbers with the HMRC API.
- **Automated Due Date**: Automatically calculates due date from the invoice date.

## 🚀 Getting Started

### Prerequisites

Make sure you have the following Python libraries:

- `fpdf`: To design the PDF layout.
- `requests`: To talk with external APIs.
- `uuid`: To generate unique invoice numbers.
- `datetime`: To handle dates.

### How to Use

1. Define the sender's and recipient's information.
2. List down the items or services you're billing for.
3. Call the `generate_invoice_adjusted()` function to produce your invoice in PDF format.

## 📚 Dependencies

- `fpdf`
- `requests`
- `uuid`
- `datetime`

## 📌 Planned Features

- **Web Front End**: A user-friendly interface to allow users to input their invoice details.
- **LLM-based Parsing**: Utilize Language Model-based parsing to intelligently interpret and generate invoices from free text inputs.

## 🤔 Thoughts
