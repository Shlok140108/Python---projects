import random

while True:
    input("Please.. Press Enter to roll the dice....")
    print("You Rolled:",random.randint(1,6))

    choice = input("Want to roll again(y/n): ")
    if choice != "y":
        print("Thanks for playing")
        break