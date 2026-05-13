NICHES = {
    "real_estate_agencies": "Real Estate Agencies",
    "general_constractors": "General Contractors",
    "construction_companies": "Construction Companies",
    "luxry_car_rentals": "Luxury Car Rentals"
}

CITIES= ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"]

SOURCES= ["yelp", "gmb"]

JUNK_PREFIXES=[
    "info@", "admin@", "noreply@", "no-reply@",
    "support@", "sales@", "hello@", "contact@",
    "enquiries@", "office@", "mail@", "team@",
    "webmaster@", "postmaster@", "accounts@",
    "reception@", "bookings@"
]

CSV_COLUMNS=[
    "Business Name", "Email", "Phone", "Website", "Source", "City", "Niche", "Verified"
]

OUTPUT_DIR="output"
LOG_DIR="logs"