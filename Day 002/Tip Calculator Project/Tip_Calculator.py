print("Welcome to the tip calculator!")
bill = float(input("What's the total of your bill? $"))
tip = int(input("What percentage tip would you like to give? ex. 10 12 15 "))
number_of_people = int(input("The bill will be split by how many people? "))

total_bill = bill * (1+tip/100)
final_amount = round(total_bill/number_of_people, 2)
print(f"Each person should pay: ${final_amount}")
