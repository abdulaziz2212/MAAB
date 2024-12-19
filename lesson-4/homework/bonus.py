import random

def rock_paper_scissors(choice):
    guess=input('Enter your choice: rock or paper or scissors: \n')
    guess=guess.lower()
    if guess not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
        return False
    print(f"Computer chose: {choice}")

    winning={
        'rock':'scissors',
        'scissors':'paper',
        'paper':'rock'
    }
    if guess==choice:
        print("it is a tie!")
        return None
    elif winning[guess]==choice:
        print('You won!')
        return True
    else:
        print('You lost!')
        return False

player=0
computer=0
while player<5 and computer<5:
    choice=random.choice(['rock','paper','scissors'])
    res=rock_paper_scissors(choice)
    if res is True: player+=1 
    elif res is False: computer+=1
if player==5: print('You won the game!')
else: print('Computer won the game')
print(f"Result is Computer:{computer} \nPlayer:{player}")

