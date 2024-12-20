def convert_cel_to_far(temp):
    far = temp * 1.8 + 32
    return far
def convert_far_to_cel(temp):
    cel = (temp - 32) * 5 / 9
    return cel

far=float(input("Enter a temperature in degrees F: "))
res=convert_far_to_cel(far)
print(f"{far} degrees F = {round(res,2)} degrees C")
cel=float(input("Enter a temperature in degrees C: "))
res=convert_cel_to_far(cel)
print(f"{cel} degrees C = {round(res,2)} degrees F")
