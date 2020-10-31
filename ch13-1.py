class Shape:
    def what_i_am(self):
        return print("I am a shape.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def calculate_perimerter(self):
        return self.width * 2 + self.len * 2

class Square(Rectangle):
    def change_size(self, w):
        self.width = self.width + w
        return self.width 


rectangle = Rectangle(35, 25)
print(rectangle.calculate_perimerter())

square = Square(15, 30)
print(square.calculate_perimerter())
print(square.change_size(5))

square.what_i_am()