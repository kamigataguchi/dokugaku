class Square:
    square_list = []

    def __init__(self, w):
        self.width = w
        self.square_list.append(self.width)
        print("{}by{}by{}by{}".format(self.width, self.width, self.width, self.width))

s1 = Square(15)
s2 = Square(45)
s3 = Square(32)

print(Square.square_list)
