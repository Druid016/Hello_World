import random

x = int(input("Enter max range: "))

feedback = ""

low = 1
high = x

while feedback != "c":

    if low == high:
        guess = low
        feedback = "c"
    else:
        guess = random.randint(low,high)
        print(f"Is your number {guess}?")
        feedback = input("Choose [c] if yes, [h] if too high, [l] if too low: ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

print(f"Your number is {guess}.")