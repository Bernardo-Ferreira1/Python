# 2D Vector Class with Special Methods
class R2Vector:
    def __init__(self, *, x, y):
        """Initialize a 2D vector with x and y components."""
        self.x = x
        self.y = y

    def norm(self):
        """Calculate and return the Euclidean norm (magnitude) of the vector."""
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        """Return a string representation of the vector as a tuple."""
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        """Return a string representation for debugging purposes."""
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        """Perform vector addition if the other object is also an R2Vector."""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        """Perform vector subtraction if the other object is also an R2Vector."""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        """Overloaded multiplication operator:
        - If multiplied by a scalar (int/float), scales the vector.
        - If multiplied by another vector, computes the dot product.
        """
        if type(other) in (int, float):  # Scalar multiplication
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):  # Dot product
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented  # If other is neither a number nor a vector

    def __eq__(self, other):
        """Check if two vectors are equal (element-wise comparison)."""
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        """Check if two vectors are not equal (opposite of __eq__)."""
        return not self == other

    def __lt__(self, other):
        """Compare vectors based on their norms (magnitude)."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        """Compare vectors based on their norms (magnitude)."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        """Less than or equal comparison using norm."""
        return not self > other

    def __ge__(self, other):
        """Greater than or equal comparison using norm."""
        return not self < other


# 3D Vector Class (Extends R2Vector)
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        """Initialize a 3D vector with x, y, and z components."""
        super().__init__(x=x, y=y)  # Initialize x and y from R2Vector
        self.z = z  # Add z component

    def cross(self, other):
        """Compute the cross product of two 3D vectors."""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        return self.__class__(**kwargs)  # Return a new R3Vector object

# --- Testing the Vector Operations ---
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)

print(f'v1 = {v1}')  # Expected output: (2, 3, 1)
print(f'v2 = {v2}')  # Expected output: (0.5, 1.25, 2)

v3 = v1 + v2
print(f'v1 + v2 = {v3}')  # Vector addition

v4 = v1 - v2
print(f'v1 - v2 = {v4}')  # Vector subtraction

v5 = v1 * v2
print(f'v1 * v2 = {v5}')  # Dot product

v6 = v1.cross(v2)
print(f'v1 × v2 = {v6}')  # Cross product
