digitlist = input("ok gimme a list of numbers and ima check if the first and last numbers are the same ")
while not digitlist.isdigit():
    print("gimme numbers u dummy ")
    digitlist = input()
if int(digitlist[0]) == int(digitlist[-1]):
    print(f"can confirm that {int(digitlist[0])} is equal to {int(digitlist[-1])}")
else:
    print(f"nah mate, {int(digitlist[0])} isn't equal to {int(digitlist[-1])}")