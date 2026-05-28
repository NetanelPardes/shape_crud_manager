class Shape:
    """
    class that defines the shape
    """
    count = 2
    def __init__(self, shape_id , shape_type):
        """
        Function initializes the shape object with input of the shape number or type
        """
        self.shape_id = shape_id
        self.shape_type = shape_type

    def get_area(self):
        """
        A function that calculates the area of ​​a general shape
        """
        pass

    def get_perimeter(self):
        """
        A function that calculates the perimeter of a general shape
        """
        pass

    def to_dict(self):
        """
        A function that defines how the shape will be stored in the system
        """
        return {"shape_id": self.shape_id, "shape_type": self.shape_type}
    
if __name__ == "__main__":
    print("=== Shape tests ===")

    shape = Shape(1, "general")

    print(shape.to_dict())
    print("Area:", shape.get_area())
    print("Perimeter:", shape.get_perimeter())