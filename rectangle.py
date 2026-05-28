from shape import Shape

import logging
logger = logging.getLogger(__name__)

class Rectangle(Shape):
    """
    A class that defines the shape Rectangle
    """
    def __init__(self, shape_id, length, width):
        """
        A function that initializes the Rectangle object
        With input of height and width
        """
        super().__init__(shape_id, "rectangle")
        
        if length <= 0 or width <=0:
            raise ValueError("The length and width must be positive.")
        
        self.length = length
        self.width = width

        logger.info("Rectangle created successfully ")
    
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
    print("=== Rectangle tests ===")

    r = Rectangle(1, 4, 6)

    print(r.to_dict())
    print("Area:", r.get_area())
    print("Perimeter:", r.get_perimeter())

    try:
        bad_rectangle = Rectangle(2, -4, 6)
    except ValueError as e:
        print("Error:", e)

    try:
        zero_rectangle = Rectangle(3, 4, 0)
    except ValueError as e:
        print("Error:", e)