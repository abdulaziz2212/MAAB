import numpy as np

vector = np.arange(1,11)

mean = np.mean(vector)
median = np.median(vector)
std = np.std(vector)


print(mean)
print(median)
print(std)
print(vector.shape)

matrix= np.arange(1,5).reshape(2,2)
print(matrix)