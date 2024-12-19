list1=list(map(int, input().strip('[]').split(", ")))
list2=list(map(int, input().strip('[]').split(", ")))
uncommon=[]
for elem in list1:
    if elem not in list2:
        uncommon.append(elem)
for elem in list2:
    if elem not in list1:
        uncommon.append(elem)
print(uncommon)