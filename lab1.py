from datetime import datetime

def calculate_age():
    current_year = datetime.now().year
    birth_year = input("Enter your birth year: ")
    age = current_year - int(birth_year)
    print("You are", age, "years old.")

calculate_age()