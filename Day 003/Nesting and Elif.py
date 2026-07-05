print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You may ride the rollercoaster, but first you must purchase the appropriate ticket for your age.")
    age = int(input("What is your age? "))
    if age < 12:
        print("You must purchase a $5 ticket.")
    elif age <= 18:
        print("You must purchase a $7 ticket.")
    elif age <= 65:
        print("You must purchase a $10 ticket.")
    else:
        print("You must purchase a $12 ticket.")
else:
    print("Sorry you have to grow taller before you can ride.")
