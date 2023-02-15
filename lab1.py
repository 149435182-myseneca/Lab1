from datetime import datetime

def calculate_age():
    current_year = datetime.now().year
    birth_year = input("Enter your birth year: ")
    try:
        age = current_year - int(birth_year)
        print("You are", age, "years old.")
    except TypeError:
        print("Please enter an int")

calculate_age()

def helloWorld():
    print('Hello World')

helloWorld()
