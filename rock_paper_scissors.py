import random

computer = random.choice(['r', 'p', 's'])
user = input("Choose [r] for rock or [p] for paper or [s] for scissors: ").lower()

def is_win(p1,p2):
    if (p1=='r' and p2=='s') or (p1=='p' and p2=='r') or (p1=='s' and p2=='p'):
        return True

if user == computer:
    print("You are in a tie!")

elif is_win(user,computer):
    if user == 'r':
        print("You Rock!")
    elif user == 'p':
        print("Paper covers it all!")
    elif user == 's':
        print("You're a cut above!")
        

else:
    print("You lose!")