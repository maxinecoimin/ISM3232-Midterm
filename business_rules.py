# Business_Rules.py
# Author: Maxine Coimin

#Rules

def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Calculates the total rental cost based on daily rate and number of days."""
    return daily_rate * days

def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Calculates the discount percentage based on the number of rental days and whether the customer is a contractor."""
    if contractor and days <= 3:
        return 0.10
    elif days >= 7:
        return 0.20
    elif days >= 3:
        return 0.10
    else:
        return 0.0

def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Calculates the final quote for a rental, applying discounts and fees as necessary."""
    cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    discounted_cost = cost * (1 - discount)
    if discounted_cost < 150.00: #waiver threshold
        return discounted_cost + 25.00 #waiver fee
    else:
        return discounted_cost

def requires_deposit(quote: float) -> bool:
    """Determines if a deposit is required based on the quote amount."""
    return quote > 1000

def needs_inspection(days: int, quote: float) -> bool:
    """Determines if an inspection is needed based on the number of days in use and quote amount."""
    return days >= 5 and quote > 800

def total_quoted(rentals: list) -> float:
    """Calculates the total quoted amount for a list of rentals."""
    total = 0
    for rental in rentals:
        total += calculate_quote(rental["daily_rate"], rental["days"], rental.get("contractor", False))
    return total

def largest_rental(rentals: list) -> str:
    """Finds the name of the customer with the largest rental quote."""
    if not rentals:
        return ""
    largest_rental = rentals[0]
    largest_quote = calculate_quote(
        largest_rental["daily_rate"],
        largest_rental["days"],
        largest_rental.get("contractor", False)
    )
    
    for rental in rentals:
        q = calculate_quote(
            rental["daily_rate"],
            rental["days"],
            rental.get("contractor", False)
        )
        if q > largest_quote:
            largest_quote = q
            largest_rental = rental
            
    return largest_rental["customer"]

def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:
    """Formats a single line of rental information for display."""
    deposit_status = "Yes" if deposit else "No"
    inspection_status = "Yes" if inspection else "No"
    return f"{customer}: Quote: ${quote:.2f}, Deposit Required: {deposit_status}, Inspection Needed: {inspection_status}"