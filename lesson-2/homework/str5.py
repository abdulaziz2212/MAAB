word=input()
vowels='aeiou'
count=0
for i in range(len(word)-1):
    if word[i] in vowels:
        count+=1
print(f"Vowels:{count}\nConsonants:{len(word)-count}")