text=input()
vowels='aieou'
for i in text:
    if i in vowels:
        text=text.replace(i,'*')
print(text)
