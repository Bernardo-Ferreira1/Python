class Rectangle:
    
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width=width

    def set_height(self,height):
        self.height=height
    
    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width+2*self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.height>50 or self.width>50:
            return 'Too big for picture.'
        output_string=('*'*self.width+'\n')*self.height
        return output_string

    def get_amount_inside(self,other):
        return (self.width // other.width) * (self.height // other.height)

class Square(Rectangle):
    
    def __init__(self,side):
        super().__init__(width=side, height=side)
    
    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self,side):
        self.width=side
        self.height=side
   
    def set_width(self, side):
        self.set_side(side)

    def set_height(self,side):
        self.set_side(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

print(rect.get_amount_inside(sq))