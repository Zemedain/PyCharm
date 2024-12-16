from helpful import please_ent, nl
import time
import random
import operator
from playsound import playsound

class Player:

    def __init__(self, name, score):

        self.name = name
        self.score = score


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

qa = {}

for _ in range(5):
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    op_symbol, op_func = random.choice(list(operations.items()))
    result = op_func(num1, num2)
    qa[f"{num1} {op_symbol} {num2} = "] = result


print("Welcome to my math game! Challenge your friend to see who is better at math!")

make = input("Enter Player 1's name: ")
please_ent(make, "a name ")
make2 = input("Enter Player 2's name: ")
please_ent(make2, "a name ")

player1 = Player(make, 0)
player2 = Player(make2, 0)

nl()

print(f"{player1.name} Start!",end="\n")

time.sleep(1)

for question in qa:
    answer = input(question)
    if answer == str(qa.get(question)):
        player1.score += 1

qa.clear()

nl()

for _ in range(5):
    num1 = random.randint(-1000, 1000)
    num2 = random.randint(-1000, 1000)
    op_symbol, op_func = random.choice(list(operations.items()))
    result = op_func(num1, num2)
    qa[f"{num1} {op_symbol} {num2} = "] = result

print(f"{player2.name} Start!",end="\n")

time.sleep(1)

for question in qa:
    answer = input(question)
    if answer == str(qa.get(question)):
        player2.score += 1

nl()

print("And the winner is....")

playsound(r"C:\Users\munth\Downloads\drumroll.mp3")
nl()

if player1.score > player2.score:
    print(f"{player1.name}!")

elif player1.score == player2.score:
    print("Draw!")
else:
    print(f"{player2.name}!")

time.sleep(2)
nl()

print(f"{player1.name}'s score: {player1.score}")
print(f"{player2.name}'s score: {player2.score}")