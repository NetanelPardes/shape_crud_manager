from shape import Shape

import logging
logger = logging.getLogger(__name__)

class Circle(Shape):
    """
    class that defines the shape Circle
    """
    PI = 3.14

    def __init__(self, shape_id ,radius):
        """
        A function that initializes the Circle object
        With radius input
        """        
        super().__init__(shape_id, "circle")
        if radius <= 0:
            raise ValueError("The radius should be positive.")
        self.radius = radius

        logger.info("Circle created successfully ")

    def get_area(self):
        """
        A function that takes a side and returns the area of ​​the circle
        """
        return Circle.PI *self.radius ** 2

    def get_perimeter(self):
        """
        A function that takes a side and returns the circumference of the circle
        """
        return 2 * self.radius * Circle.PI

    def to_dict(self):
        """
        A function that defines how the shape will be stored in the system
        """
        data = super().to_dict()
        data["radius"] = self.radius
        return data 
    
if __name__ == "__main__":
    """
    Tests that check whether the shape class works
    """
    c = Circle(5,12)
    print(c.to_dict())
    print(c.get_area())
    print(c.get_perimeter())