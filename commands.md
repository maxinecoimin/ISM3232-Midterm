# Terminal Record: Ridgeline Tool Rental

## 1. Building the project
# Author's Note: I pulled these directly from my Terminal (erasing the pwd results) and have added additional notes throughout as my process was all over the place.
Day 1

    cd ~/ism3232
    pwd
    mkdir midterm
    pwd
    cd ~/ism3232/midterm
    python3 -m venv .venv && source .venv/bin/activate
    (.venv) MaxinesLaptop% touch business_rules.py main.py commands.md README.md requirements.txt .gitignore tests__init__.py tests/test_business_rules.py (the test ones were unsusccessful)
    touch tests
    code business_rules.py
    code main.py
    python3 main.py
    git init
    git add README.md
    git commit -m "first commit which inclues the business rules fully set up and the main page in progress while I work through some errors" (did not realize only the readme went through to git hub)
    git branch -M main
    git remote add origin https://github.com/maxinecoimin/ISM3232-Midterm.git
    git push -u origin main
Day 2
    python3 main.py (4 times while fixing errors)
    pwd
    git init
    git add .
    git commit -m "Adding business_rules.py and main.py"
    git remote add origin https://github.com/maxinecoimin/ISM3232-Midterm.git
    git branch -M main
    git push -u origin main (this push included everything)

    # Fixing the tests
    mkdir tests && touch tests/__init__.py tests/test_business_rules.py
    rm tests
    mkdir tests
    touch tests/__init__.py tests/test_business_rules.py
    ls tests
    git add .
    git commit -m "Updated README with project details ans fixed tests so that it's a directory, not a file"
    git push

## 2. The virtual environment
It shows that python3 is in the virtual environment while idicating that the virtual environment is active with the (.venv) prefix

## 3. The project structure
The pycache folder is in the tree but in the GitHub repository because of the .gitignore file

## 4. Every function and test
Business_rules.py has defined 8 functions and tests/test_business_rules.py defines 26 tests.

## 5. Which files print
## 6. The commit history