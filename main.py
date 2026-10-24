# Main.py

from business_rules import (
    calculate_quote,
    format_rental_line,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)

rentals = [
    {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
    {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
    {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    {"customer": "Dvorak", "daily_rate": 120.00, "days": 10, "contractor": False},
    {"customer": "Eastman", "daily_rate": 210.00, "days": 8, "contractor": True},
    {"customer": "Fujita", "daily_rate": 250.00, "days": 4, "contractor": False},
    {"customer": "Garza", "daily_rate": 95.00, "days": 5, "contractor": True},
    {"customer": "Hughes", "daily_rate": 200.00, "days": 7, "contractor": False},
]

print("Ridgeline Tool Rental - Rental Report")
for rental in rentals:
    quote = calculate_quote(
        rental["daily_rate"], rental["days"], rental.get("contractor", False)
    )
    deposit = requires_deposit(quote)
    inspection = needs_inspection(rental["days"], quote)
    print(format_rental_line(rental["customer"], quote, deposit, inspection))
print(f"Rentals: {len(rentals)}")
print(f"Total Quoted: ${total_quoted(rentals):.2f}")
print(f"Average Quote: ${total_quoted(rentals) / len(rentals):.2f}")
print(f"Largest Quote: {largest_rental(rentals)}")
print(
    f"Deposits Required: {sum(1 for rental in rentals if requires_deposit(calculate_quote(rental['daily_rate'], rental['days'], rental.get('contractor', False))))}"
)
print(
    f"Inspections Required: {sum(1 for rental in rentals if needs_inspection(rental['days'], calculate_quote(rental['daily_rate'], rental['days'], rental.get('contractor', False))))}"
)
