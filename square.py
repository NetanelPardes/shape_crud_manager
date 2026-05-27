from shape import Shape

class Square(Shape):
    """
    A class that defines the shape Square
    """
    def __init__(self, shape_id,side):
        """
        A function that initializes the Square object
        With side input
        """
        super().__init__(shape_id, "Square")
        self.side = side

    def get_area(self):
        """
        A function that takes a side and returns the area of ​​a square
        """
        return self.side * self.side

    def get_perimeter(self):
        """
        A function that takes a side and returns the perimeter of a square
        """
        return (self.side + self.side)*2

    def to_dict(self):
        """
        A function that defines how the shape will be stored in the system
        """
        data = super().to_dict()
        data["side"] = self.side
        return data

if __name__ == "__main__":
    """
    Tests that check whether the shape class works
    """
    s = Square(4,8)
    print(s.to_dict())
    print(s.get_area())
    print(s.get_perimeter())