# Tests for Business Rules

from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    format_rental_line,
    get_rental_discount,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)


# Total rental cost tests
def test_calculate_rental_cost():
    assert round(calculate_rental_cost(100, 5)) == 500


# Rental discount tests
def test_get_rental_discount_single_day():
    assert get_rental_discount(1) == 0.0


def test_get_rental_discount_short_term():
    assert get_rental_discount(3) == 0.10


def test_get_rental_discount_middle_limit():
    assert get_rental_discount(6) == 0.10


def test_get_rental_discount_long_term():
    assert get_rental_discount(7) == 0.20


def test_get_rental_discount_contractor():
    assert get_rental_discount(1, True) == 0.10


def test_get_rental_discount_contractor_long_term():
    assert get_rental_discount(9, True) == 0.20


# Quote calculation tests with different waivers and discounts
def test_calculate_quote():
    assert round(calculate_quote(90, 2), 2) == 180


def test_calculate_quote_with_discount():
    assert round(calculate_quote(100, 7), 2) == 560


def test_calculate_quote_with_waiver_required():
    assert round(calculate_quote(50, 3), 2) == 160


def test_calculate_quote_with_no_discount_but_waiver_required():
    assert round(calculate_quote(55, 2), 2) == 135


def test_calculate_quote_at_waiver_threshold():
    assert round(calculate_quote(41.75, 4), 2) == 150.30


# Deposit requirement tests
def test_requires_deposit_above_limit():
    assert requires_deposit(1500) == True


def test_requires_deposit_below_limit():
    assert requires_deposit(900) == False


def test_requires_deposit_at_limit():
    assert requires_deposit(1000) == False


# Inspection requirement tests
def test_needs_inspection_long_term_high_quote():
    assert needs_inspection(6, 900) == True


def test_needs_inspection_short_term_high_quote():
    assert needs_inspection(3, 900) == False


def test_needs_inspection_term_at_quote_threshold():
    assert needs_inspection(5, 800) == False


def test_needs_inspection_threshold_term_lower_quote():
    assert needs_inspection(5, 799) == False


def test_needs_inspection_threshold_term_higher_quote():
    assert needs_inspection(5, 801) == True


def test_needs_inspection_long_term_low_quote():
    assert needs_inspection(7, 700) == False


# Total quoted amount tests
def test_total_quoted():
    rentals = [
        {
            "customer": "Maxine",
            "daily_rate": 65,
            "days": 2,
            "contractor": False,
        },  # 155 w/ waiver
        {
            "customer": "Jaime",
            "daily_rate": 100,
            "days": 2,
            "contractor": True,
        },  # 180 w/ discount
        {
            "customer": "Mariah",
            "daily_rate": 75,
            "days": 8,
            "contractor": False,
        },  # 480 w/ discount
    ]
    assert round(total_quoted(rentals), 2) == 815.00


# Largest rental tests
def test_largest_rental():
    rentals = [
        {
            "customer": "Maxine",
            "daily_rate": 65,
            "days": 2,
            "contractor": False,
        },  # 155 w/ waiver
        {
            "customer": "Jaime",
            "daily_rate": 100,
            "days": 2,
            "contractor": True,
        },  # 180 w/ discount
        {
            "customer": "Mariah",
            "daily_rate": 75,
            "days": 8,
            "contractor": False,
        },  # 480 w/ discount
    ]
    assert largest_rental(rentals) == "Mariah"


def test_largest_rental_empty():
    rentals = []
    assert largest_rental(rentals) == ""


def test_largest_rental_tie_chooses_first():
    rentals = [
        {"customer": "Maxine", "daily_rate": 150, "days": 3, "contractor": False},
        {"customer": "Jaime", "daily_rate": 100, "days": 2, "contractor": True},
        {"customer": "Mariah", "daily_rate": 90, "days": 5, "contractor": False},
    ]
    assert largest_rental(rentals) == "Maxine"


# Formatting rental line tests
def test_format_rental_line():
    customer = "Maxine"
    quote = 500.00
    deposit = False
    inspection = False
    assert (
        format_rental_line(customer, quote, deposit, inspection)
        == "Maxine: Quote: $500.00, Deposit Required: No, Inspection Needed: No"
    )
