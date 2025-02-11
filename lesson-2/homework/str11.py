text=input()
a=sum([text[i].isdigit() for i in range(len(text))])
print(a)