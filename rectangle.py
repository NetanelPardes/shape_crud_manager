from shape import Shape

class Rectangle(Shape):
    """
    A class that defines the shape Rectangle
    """
    def __init__(self, shape_id, length, width):
        """
        A function that initializes the Rectangle object
        With input of height and width
        """
        super().__init__(shape_id,"Rectangle")
        self.length = length
        self.width = width
    
    def get_area(self):
        """
        A function that takes a side and returns the area of ​​the rectangle
        """
        return self.length * self.width
    
    def get_perimeter(self):
        """
        A function that takes a side and returns the perimeter of the rectangle
        """
        return (self.length + self.width)*2
    
    def to_dict(self):
        """
        A function that defines how the shape will be stored in the system
        """
        data = super().to_dict()
        data["length"] = self.length
        data["width"] = self.width
        return data
    
if __name__ == "__main__":
    """
    Tests that check whether the shape class works
    """
    r = Rectangle(3,3,4)
    print(r.to_dict())
    print(r.get_area())
    print(r.get_perimeter())