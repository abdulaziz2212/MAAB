import numpy as np

A=np.array([
    [10,-2,3],
    [-2,8,-1],
    [3,-1,6]
])

B=np.array([12,-5,15])

res=np.linalg.solve(A,B)
print(f"I1 is {res[0]} \nI2 is {res[1]} \nI3 is {res[2]}")


