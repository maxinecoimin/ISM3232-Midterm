# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Maxine Coimin
- **Version:** Version 1
- **Date:** October 24, 2026

## What This Program Does
This coding project is designed to calculate the rental cost, deposit, and advise the inspection requirements for Ridgeline Tool Rentals

## Business Rules
1. The cost of the rental is determined by the daily rate multiplied by the number of days
2. The rate is discounted starting from the 3rd day at 10% and more than 7 days at 20%
3. Licensed contractors always get, at minimum, a 10% discount
4. If the total cost is less than $150, a $25 damage waiver is added
5. If the quote is $1,000 or more, it requires a deposit
6. If the rental is run for 5+ days and quoted at over $800, a pickup inspection is required

## How to Run
### To create the virtual environment
python3 -m venv .venv
source .venv/bin/activate
### Install requirements
pip install -r requirements.txt
### Run the program
python3 main.py

## How to Test
ruff format .
ruff check .
pytest -v

## Files in This Repository
1. Tests
2. .gitignore
3. README.md
4. Business_rules.py
5. Commands.md
6. Main.py
7. Requirements.txt

## AI Use Statement
I did not use AI for this midterm project.