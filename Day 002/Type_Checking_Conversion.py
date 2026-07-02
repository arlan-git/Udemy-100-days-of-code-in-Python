# Types function in use

# <class str>
print(type("Hello"))

# <class int>
print(type(123))

# <class float>
print(type(12.345))

# <class bool>
print(type(True))

print(int("123") + int(456))

# You can convert data into different data types using special functions. e.g.
float()
int()
str()

name_of_the_user = input("Please enter your name: ")
length_of_the_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) #str
print(type(length_of_the_name)) #int

print("Number of letters in your name: " + str(length_of_the_name))
