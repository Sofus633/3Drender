import math

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, other):
        assert type(other) == Vector3
        return Vector3(self.x - other.x ,self.y - other.y, self.z - other.z)

    def __add__(self, other):
        assert isinstance(other, Vector3)
        return Vector3(self.x + other.x ,self.y + other.y, self.z + other.z)
    
    def __mul__(self, scalar):
        assert type(scalar) == int or type(scalar) == float
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar):
        assert type(scalar) == int or type(scalar) == float
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar) 
    
    def length(self):
        return math.sqrt(self.x **2 + self.y**2 + self.z**2)
    
    def get(self):
        return [self.x, self.y, self.z]
    
    def dot(self, other):
        assert type(other) == Vector3
        return self.x * other.x + self.y * other.y + self.z * other.z



class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __sub__(self, other):
        assert type(other) == Vector2
        return Vector2(self.x - other.x ,self.y - other.y)

    def __add__(self, other):
        assert type(other) == Vector2
        return Vector2(self.x + other.x ,self.y + other.y)
    
    def __mul__(self, scalar):
        assert type(scalar) == int or type(scalar) == float
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        assert type(scalar) == int or type(scalar) == float
        return Vector2(self.x / scalar, self.y / scalar) 
    
    def length(self):
        return math.sqrt(self.x **2 + self.y**2)
    
    def get(self):
        return [self.x, self.y]
    
    def dot(self, other):
        assert type(other) == Vector2
        return self.x * other.x + self.y * other.y


