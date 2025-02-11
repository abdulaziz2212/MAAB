import numpy as np

def power(x,y):
    return x**y

a=[2, 3, 4, 5]
b=[1, 2, 3, 4]

vectorized_power=np.vectorize(power)
res=vectorized_power(a,b)
print(res)