import math
class Vector:
    def __init__(self, *args):
        self.args=list(args)

    def __add__(self,other):
        if len(self.args)!=len(other.args):
            raise ValueError("vectors must have same dimension")
        new_args=[a+b for a,b in zip(self.args,other.args)]
        return Vector(*new_args)
    
    def __mul__(self,other):
        if isinstance(other,(int,float)):
            new_args=[a*other for a in self.args]
            return Vector(*new_args)
                   
        elif isinstance(other,Vector):
            if len(self.args)!=len(other.args):
                raise ValueError("vectors must have same dimension")
            return sum(a*b for a,b in zip(self.args,other.args))
        else:
            raise TypeError("Unsupported operand type for multiplication")
    
    def __rmul__(self,other):
        if isinstance(other,(int,float)):
            new_args=[a*other for a in self.args]
            return Vector(*new_args)
        else:
            raise TypeError("Unsupported operand type for multiplication")
        
    def __sub__(self,other):
        if len(self.args)!=len(other.args):
            raise ValueError("vectors must have same dimension")
        new_args=[a-b for a,b in zip(self.args,other.args)]
        return Vector(*new_args)
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.args))
    
    def normalize(self):
        div=self.magnitude()
        if div==0:
            raise ValueError("cannot normalize the zero vector!")
        new_args=[a/div for a in self.args]
        return Vector(*new_args)

    def __str__(self):
        return f"Vector({', '.join(map(str, self.args))})"
    

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)  
# Substraction
v4 = v2 - v1
print(v4) 
# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801) 