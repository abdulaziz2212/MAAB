password=input('Enter your password: \n')
if len(password)<8:
    print('Password is too short')
elif password.islower():
    print("Password must contain an uppercase letter.")
else:
    print('Password is strong: ')