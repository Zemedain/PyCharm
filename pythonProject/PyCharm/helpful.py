def please_ent(variable, custom_message):

    while variable == "" or variable == " ":
        print(f"Please enter {custom_message} ",end="")
        variable = input()


def nl():
    print("\n")