from shape import Shape

import logging
logger = logging.getLogger(__name__)

class Square(Shape):
    """
    A class that defines the shape Square
    """
    def __init__(self, shape_id,side):
        """
        A function that initializes the Square object
        With side input
        """
        super().__init__(shape_id, "square")
        if side <= 0:
            raise ValueError("The side must be positive.") 
        self.side = side

        logger.info("Square created successfully ")

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
    print("=== Square tests ===")

    s = Square(1, 5)

    print(s.to_dict())
    print("Area:", s.get_area())
    print("Perimeter:", s.get_perimeter())

    try:
        bad_square = Square(2, -3)
    except ValueError as e:
        print("Error:", e)

    try:
        zero_square = Square(3, 0)
    except ValueError as e:
        print("Error:", e)