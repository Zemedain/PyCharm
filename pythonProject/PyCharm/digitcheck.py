basedlist = input("ok gimme a list of numbers and ima check if the first and last numbers are the same ")
while not basedlist.isdigit():
    print("gimme numbers u dummy ")
    basedlist = input()
if int(basedlist[0]) == int(basedlist[-1]):
    print(f"can confirm that {int(basedlist[0])} is equal to {int(basedlist[-1])}")
else:
    print(f"nah mate, {int(basedlist[0])} isn't equal to {int(basedlist[-1])}")