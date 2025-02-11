import numpy as np

def fahrenheitToCalcius(x):
    c=(x-32)*5/9
    return c

vectorized_F_to_Celc=np.vectorize(fahrenheitToCalcius)
celcius_array=vectorized_F_to_Celc(np.array([32, 68, 100, 212, 77]))
print(celcius_array)