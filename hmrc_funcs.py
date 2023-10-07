import requests
from requests.auth import HTTPBasicAuth
import re


def verify_company_details(company_number, provided_name, provided_address, provided_postcode):
    # API endpoint
    url = f"https://api.company-information.service.gov.uk/company/{company_number}"

    # Authentication details
    api_key = "17e97701-02d0-4d75-ba41-18e83a9f6dbe"
    auth_details = HTTPBasicAuth(api_key, "")  # Password is blank

    # Fetch company details from the API
    response = requests.get(url, auth=auth_details)
    
    # Check for 404 error
    if response.status_code == 404:
        return {"error": "Company not found"}

    data = response.json()

    # Extract company name and registered office address from the API response
    official_name = data["company_name"]
    official_address = data["registered_office_address"]["address_line_1"]
    official_postcode = data["registered_office_address"]["postal_code"]

    # Verify provided name, address, and postcode
    name_verified = official_name == provided_name
    address_verified = official_address == provided_address
    postcode_verified = official_postcode == provided_postcode

    return {
        "name_verified": name_verified,
        "address_verified": address_verified,
        "postcode_verified": postcode_verified,
        "official_name": official_name,
        "official_address": official_address,
        "official_postcode": official_postcode
    }


def verify_vat_number(vat_number):
    # Extract only the numeric part of the VAT number
    vat_numeric = ''.join(re.findall(r'\d+', vat_number))
    
    # Use the HMRC API to verify the VAT number
    url = f"https://api.service.hmrc.gov.uk/organisations/vat/check-vat-number/lookup/{vat_numeric}"
    response = requests.get(url)
    
    verification_result = {
        "vat_verified": False,
        "official_vat": vat_number,
        "official_name": None
    }

    if response.status_code == 200:
        data = response.json()
        # Check if the response contains the target's vatNumber
        if "target" in data and "vatNumber" in data["target"] and data["target"]["vatNumber"] == vat_numeric:
            verification_result["vat_verified"] = True
            verification_result["official_vat"] = data["target"]["vatNumber"]
            verification_result["official_name"] = data["target"].get("name", None)

    return verification_result

