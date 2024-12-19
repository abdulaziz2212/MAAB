import random
num=random.randint(1,101)

def game(num):
    guess=int(int(input('Enter your guess: \n')))
    
    if guess>num:
        print('Too high!')
        return False
    elif guess<num:
        print('Too low')
        return False
    else:
        print('You guessed right!')
        return True
    

count=0    
while count<10:
    count+=1
    if game(num):
        break
else:
    print(f"Game over! The answer was {num}")