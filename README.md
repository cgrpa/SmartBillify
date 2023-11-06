# 🧾 SmartBillify

SmartBillify is a modest weekend project I've embarked on, aimed at generating PDF invoices with a touch of automation in Python.

## 🌟 Features

- **Generate PDF Invoices**: Simple and clean invoice design.
- **Companies House Lookup**: Verify company details in a jiffy. Green indicates validation, red indicates refusal of validation.
- **VAT Verification**: Double-check VAT numbers with the HMRC API. Green indicates validation, red indicates refusal of validation.
- **Automated Due Date**: Automatically calculates due date from the invoice date.

Example PDF:
![invoice_adjusted_INV12345.pdf](https://github.com/cgrpa/SmartBillify/files/12838258/invoice_adjusted_INV12345.pdf)
![Capture (1) (1)](https://github.com/cgrpa/SmartBillify/assets/95618126/3675bf18-cde2-46f0-bcee-d9cd562ba679)

# 🧾 SmartBillify

SmartBillify is a modest weekend project I embarked on, aimed at generating PDF invoices with a touch of automation in Python.

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

It was a delightful weekend exercise! There's a lot of scope for improvement, bugs to fix and features to add. Any feedback or suggestions are welcome.
