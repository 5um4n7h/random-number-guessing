import random

print("Number guessing game")

number = random.randint(1, 9)

chances = 0

print("Guess a number (between 1 and 9):")
while chances < 3:
    guess = int(input())
    chances += 1
    if guess == number:
        print("Congratulation WON!!!")
        exit(0)
    if chances < 3:
        print("Worng!, Guess ag.")
        hjdxhbdbhdhbd


print("YOU LOSE!!! The number is", number)
