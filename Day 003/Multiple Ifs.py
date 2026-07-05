print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You may ride the rollercoaster, but first you must purchase the appropriate ticket for your age.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5 a ticket.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7 a ticket.")
    elif age <= 65:
        bill = 10
        print("Senior citizen tickets are $10 a ticket.")
    else:
        bill = 12
        print("Adult tickets are $12 a ticket.")

    take_photo = input("Would you like a photo taken? Type 'Y' for Yes or 'N' for No.")
    if take_photo == "Y":
        # $3 added to rider's bill
        bill = bill + 3
        print("$3 will be added to your final bill.")

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
