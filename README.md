# SmartBillify
Description
Smart Billify is a Python application designed to automate the creation of PDF invoices. It integrates with external APIs for VAT number verification and company details verification, enhancing the accuracy and authenticity of the invoices produced.

Features
Dynamic Invoice Creation: Generate PDF invoices on-the-fly based on input data such as sender details, recipient details, and itemized lists.
Verification with Companies House API: Automatically verify company details and addresses using the Companies House API to ensure recipient information's authenticity.
VAT Number Verification: Ensure VAT numbers are genuine by checking them against the HMRC API.
Dynamic Date Handling: Auto-generate due dates based on invoice dates.
Custom Formatting: The PDF invoices are styled and structured for clarity and professionalism.
Usage
Set up the sender's details, including company information and VAT number.
Specify the recipient's details, such as name, address, and company details.
List out the items or services provided, including descriptions, quantities, and prices.
Call the generate_invoice_adjusted() function to produce a PDF invoice.
Sample Output
The generated invoice includes:

Sender and recipient details.
A table of items or services provided with associated costs.
Calculated totals including net, tax (VAT), and overall total.
Verification markers (like a green star) indicating the authenticity of company details and VAT numbers.
Dependencies
fpdf: For generating PDFs.
requests: To make HTTP requests to external APIs.
uuid: To generate unique invoice numbers.
datetime: To handle dates and date arithmetic.
Future Enhancements
Integration with more APIs for expanded verification.
Customizable invoice templates and styles.
Ability to handle different tax rates and currencies.
Enhanced error handling and logging.
