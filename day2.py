#functions
restaurants=["KFC", "McDonald's", "Subway", "Pizza Hut", "Burger King"]
alphabetical_restaurants=sorted(restaurants)
print("Restaurants in alphabetical order:", alphabetical_restaurants)

numbers=[5, 2, 9, 1, 7]
largest_number=max(numbers)
print("The largest number is:", largest_number)
smallest_number=min(numbers)
print("The smallest number is:", smallest_number)
# module=python file with functions and variables
# python built-in functions
# len() function
print("The number of restaurants is:", len(restaurants))
print("The number of numbers is:", len(numbers))

"""#  importing a module
import os
print(type(os))
import string
print(type(string))"""


""" # call help
print(help(os))
# using an os function
print(os.getcwd())  # prints the current working directory
# assign to a variable
current_directory = os.getcwd()
print("Current working directory:", current_directory)
# changing directory
os.chdir("..")  # changes to the parent directory
print("Changed directory to:", os.getcwd())
# module attributes
print("OS module name:", os.name)
print(os.environ)  # prints environment variables """
# string module
import string
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)
#packages = collection of modules also called a library publically valiable and free
# function = to perform a task | methods = functions that belong to an object
"""def average(values):
    # calculate the average of a list of numbers
    average_value = sum(values) / len(values)
   
    rounded_average = round(average_value, 2)
    return rounded_average
marks=[85, 90, 78, 92, 88]
average_marks=average(marks)
print("The average marks are:", average_marks)

def validate_age(age):
    if age<=100:
        return True
    else:
        return False
validation_result=validate_age(25)
if validation_result:
    print("Age is valid.")

def char_string(string):
    if len(string)>0:
        return True
    else:
        return False
string_result=char_string("Hello, World!")
print("String is valid:", string_result)

def conversion(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
temperature_celsius=25
temperature_fahrenheit=conversion(temperature_celsius)
print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit}°F")
"""
# file handling
# Writing to a file
# file=open("notes.txt","r")
# file.close()
"""
"r" = read
"w" = write
"a" =append add to end of file
"x" = create a new file
"""
# with open("notes.text","r") as file:
# print(file.read())
with open("notes.txt","w") as file:
    file.write("heelo! python\n")
with open("notes.txt","a") as file:
    file.write("learn python\n")

with open("notes.txt","r") as file:
     print(file.read())

with open("notes.txt","r") as file:
     print(file.readline())
     print(file.readline())

""" | Method        | Returns         | Best for                      |
| ------------- | --------------- | ----------------------------- |
| `read()`      | One string      | Read the entire file          |
| `readline()`  | One string      | Read one line at a time       |
| `readlines()` | List of strings | Work with all lines as a list |
"""