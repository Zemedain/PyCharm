import time
from helpful import nl

questions = {"Which of the following is a hydrocarbon?" : "B",
             "Which of these formulas do you use when you are not given time?" : "D",
             "Who is the lead singer of the 'Sabaton' band?" : "D",
             "The Chernobyl nuclear reactor accident happened in the year:" : "A"}

options = [["A. MgO", "B. CH3OH", "C. C12O5H11", "D. H2O2"],
           ["A. x = at^2 + v0t + x0", "B. E = mc^2", "C. x - x0 = at^2 + v0t", "D. v^2 - v0^2 = 2a.x-x0"],
           ["A. Par", "B. Dwayne 'The Rock' Johnson", "C. Kevin Hart", "D. Joakim"],
           ["A. 1986", "B. 670 BC", "C. 1939", "D. 1945"]]

begin = input("Welcome to my quiz game. Enter 'Y' to begin. ").upper()

while begin == "Y":
    answer = 1
    correct_answer = 0
    for question in questions:
        print(question)
        for option in options[answer-1]:
            time.sleep(1.5)
            print(option)
        useranswer = input(" ")
        if useranswer == questions.get(question):
            correct_answer += 1

        answer += 1
        if answer == 3:
            begin = False

nl()
print("The answers are: ", end="")
time.sleep(1)
for i in questions:
    print(questions.get(i), end=" ")
nl()
time.sleep(1.5)
print(f"Correct answers: {correct_answer}")