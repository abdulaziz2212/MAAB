text=input()
used='aioue'
new=''
count=0
for i in text[:-1]:
    count+=1
    new+=i
    if count>=3 and i not in used:
        new+='_'
        count=0
        used+=i
new+=text[-1]
print(new)

