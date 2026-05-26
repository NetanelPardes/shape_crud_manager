from shape import Shape

class Circle(Shape):
    PI = 3.14

    def __init__(self, shape_id, shape_type ,radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius

    def get_area(self):
        return Circle.PI *self.radius ** 2

    def get_perimeter(self):
        return 2 * self.radius * Circle.PI

    def to_dict(self):
        data = super().to_dict()
        data["radius"] = self.radius
        return data 