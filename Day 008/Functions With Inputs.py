# def greet():
    #print("World Cup 2026, Semifinals.")
    #print("France vs Spain")
    #print("Argentina vs England")

#greet()

def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"How are you {name}?")

greet_with_name("Pedro")

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

life_in_weeks(12)
