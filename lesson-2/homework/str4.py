word=input()
l=len(word)//2
flag=1
for i in range(l):
    if word[i]!=word[len(word)-1-i]:
        print(f'The word {word} is not palindrome')
        flag=0
        break
if flag: print(f'The word {word} is palindrome')