# 🧾 Invoice Generator

Invoice Generator is a Python-powered tool designed to streamline and automate the process of creating professional PDF invoices.

## 🌟 Features

- **Dynamic Invoice Creation**: Craft PDF invoices on-the-fly.
- **Companies House Integration**: Confirm company details and addresses with ease.
- **VAT Verification**: Authenticate VAT numbers via the HMRC API.
- **Automated Date Handling**: Set due dates based on invoice dates without manual calculations.
- **Stylish PDF Output**: Elegantly styled invoices for a professional look.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following libraries installed:

- `fpdf`: For crafting the PDFs.
- `requests`: To communicate with external APIs.
- `uuid`: For unique invoice number generation.
- `datetime`: For date manipulations.

### Basic Usage

1. 📋 Define the sender and recipient details.
2. 📦 Enumerate the services/products provided.
3. 🧮 Call `generate_invoice_adjusted()` to get your invoice as a PDF.

## 📖 Sample

The output invoice will showcase:

- Detailed sender and recipient sections.
- A clear breakdown of services/products with costs.
- Net, Tax (VAT), and total amounts.
- Verification markers to indicate validated data.

## 📚 Dependencies

This project leans on several external libraries:

- `fpdf`
- `requests`
- `uuid`
- `datetime`

## 🌱 Future Enhancements

- Dive deeper with more API integrations.
- Choose from a variety of invoice styles.
- Multicurrency and varied tax rate support.
- Robust error handling and detailed logs.
