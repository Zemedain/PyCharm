import random
import time

#------------------------------------------------------------------------------------------------------------------

words = ["apple", "needle", "secretary", "immune", "carbohydrate", "revolutionary", "exception", "refrigerator",
         "conditioner", "fahrenheit", "psychology", "indigenous"]

man = {0: ("   ",
           "   ",
           "   "),
       1: (" o ",
           "   ",
           "   "),
       2: (" o ",
           " | ",
           "   "),
       3: (" o ",
           "/| ",
           "   "),
       4: (" o ",
           "/|\\",
           "   "),
       5: (" o ",
           "/|\\",
           "/  "),
       6: (" o ",
           "/|\\",
           "/ \\")}
#------------------------------------------------------------------------------------------------------------------
print("Welcome to the hangman game.")

time.sleep(1.5)

print("Guess a letter of the word until you reveal the word before the stick figure is completed.")

time.sleep(2.5)

print("Good luck.")

time.sleep(1.5)
#------------------------------------------------------------------------------------------------------------------


def display_man(wrong_guess):
    for line in man[wrong_guess]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def main():
    word = random.choice(words)
    hint = ["_"] * len(word)
    wrong_guess = 0
    guessed_letters = set()

    while True:

        display_man(wrong_guess)
        display_hint(hint)
        answer = input("Enter a letter: ").lower()

        if len(answer) != 1 or answer.isdigit():
            print("Invalid input")
            continue

        if answer in guessed_letters:
            print(f"You have already guessed {answer}")
            continue

        guessed_letters.add(answer)

        if answer in word:
            for i in range(len(word)):
                if word[i] == answer:
                    hint[i] = answer
        else:
            wrong_guess += 1

        if "_" not in hint:
            print("You win!")
            time.sleep(1.5)
            print(f"The word is: {word}")
            time.sleep(1.5)
            replay = input("Would you like to play again? (Y to accept): ").lower()
            if replay == "y":
                main()
            else:
                break

        if wrong_guess == 6:
            display_man(6)
            print("You lose!")
            time.sleep(1.5)
            print(f"The word was: {word}")
            time.sleep(1.5)
            replay = input("Would you like to play again? (Y to accept): ").lower()
            if replay == "y":
                main()
            else:
                break


#------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
