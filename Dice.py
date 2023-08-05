import random

Confirm = True

while Confirm == True:
    question = input("Would you like to roll the dice? ('y' or 'n'): ")

    if question == 'y':
        Confirm = True
    elif question == 'n':
        break
    else:
        print("Reset program")
        break
    integer = random.randint(1,6)
    for i in range(0,integer):
       print("[    •    ]")
