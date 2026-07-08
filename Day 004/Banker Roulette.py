import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1 randomly select a name and print the name
#random_name = random.choice(friends)
print(random.choice(friends))

#Option 2 randomly select a name and print int for the name
random_name_index = random.randint(0,4)
print(friends[random_namme_index])
#print(random_name_index)

