from arithmetic import *

operator = input("Please select an arithmetical operator ")
while operator not in ("+", "-", "*", "/"):
     operator = input("Invalid operator. Please try again ")

if operator == "+":
    numbers = input("Insert the numbers that you want to add (separated by space): ")
    numbers = list(map(int, numbers.split()))
    print(add(*numbers))

elif operator == "-":
    numbers = input("Insert the numbers that you want to subtract (separated by space): ")
    numbers = list(map(int, numbers.split()))
    print(subtract(*numbers))

elif operator == "*":
    numbers = input("Insert the numbers that you want to multiply (separated by space): ")
    numbers = list(map(int, numbers.split()))
    print(multiply(*numbers))

else:
    numbers = input("Insert the numbers that you want to divide (separated by space): ")
    numbers = list(map(int, numbers.split()))
    print(divide(*numbers))