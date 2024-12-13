#1
user=input()
password=input()
if user and password:
    print('Non empty!')
else:
    print("empty")
#2
a,b=map(float, input().split())
print('They are equal') if a==b else print('They are not equal')

#3
a=int(input())
print('positive and even') if (a>0 and a%2==0) else print("no")

#4
nums=list(map(float, input().split()))
print('yes') if len(nums)==len(set(nums)) else print('no')

#5
a,b=map(str, input().split())
print('yes') if len(a)==len(b) else print('no')

#6
a=int(input())
print('divisible by 3 and 5') if a%15==0 else print('no')

#7
a,b=map(float, input().split())
if a<10 or a>20:
    a=input('enter a number between 10 and 20:  ')
if b<10 or b>20:
    b=input('enter a number between 10 and 20:  ')
print('yes') if a+b>50.8 else print('no')