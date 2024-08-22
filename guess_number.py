import random

x = int(input("Enter the maximum number for range: "))

random_number = random.randint(1,x)

guess = 0

while guess != random_number:
    guess = int(input(f'Enter a number between 1 and {x}: '))
    if guess < random_number:
        print("Your guess is smaller! Guess again!!")
    elif guess > random_number:
        print("Your guess is bigger! Guess again!!")

print("You guessed it right!")