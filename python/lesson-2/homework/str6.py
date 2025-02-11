a,b=map(str, input().split())
if a in b:
    print(f"{b} contains {a}")
elif b in a:
    print(f"{a} contains {b}")
else: print("The strings didn't catch")