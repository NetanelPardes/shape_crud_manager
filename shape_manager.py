import json
import logging
logger = logging.getLogger(__name__)

from circle import Circle
from rectangle import Rectangle
from square import Square

class ShapeManager:
    """
    A class that manages the shapes
    """
    def __init__(self):
        """
        A function initializes the shapes in a json file
        """
        self.shapes = []
        self.load_from_json()

        logger.info("Shape Manager created successfully")

    def create_shape(self, shape_dict):
        """

        """
        if shape_dict["shape_type"] == "square":
            my_shape = Square(shape_dict["shape_id"],shape_dict["side"])
            #print(my_square.to_dict())
        
        elif shape_dict["shape_type"] == "rectangle":
            my_shape = Rectangle(shape_dict["shape_id"], shape_dict["length"] , shape_dict["width"])
        
        elif shape_dict["shape_type"] == "circle":
            my_shape = Circle(shape_dict["shape_id"],shape_dict["radius"])
        
        self.shapes.append(my_shape)
        self.save_to_json()

    def get_all_shapes(self):
        """
    
        """
        return self.shapes

    def update_shape(self, shape_id, new_data):
        """
    
        """
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                if shape.shape_type == 'square':
                    shape.side = new_data['side']

                elif shape.shape_type == 'rectangle':
                    shape.length = new_data['length']
                    shape.width = new_data['width']

                elif shape.shape_type == 'circle':
                    shape.radius = new_data['radius']
                
                self.save_to_json()
                break
        

                   
    def delete_shape(self, shape_id):
        """
    
        """
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                break
            

    def save_to_json(self):
        """
    
        """
        with open("shapes.json", "w", encoding="utf-8") as file:
            json.dump([shape.to_dict() for shape in self.shapes], file, indent=4)
    
    def find_shape_by_id(self, shape_id):
        """
        
        """
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                return shape.shape_type
        return None

    def get_id(self):
        """
        
        """
        if not self.shapes:
            return 1
        return max(shape.shape_id for shape in self.shapes) + 1
        
    def load_from_json(self):
        """
    
        """
        try:
            with open("shapes.json", "r", encoding="utf-8") as file:
                logger.info("Loading shapes from %s" ,file.name)
                shapes_data = json.load(file)

                for shape in shapes_data:
                    self.create_shape(shape)

        except FileNotFoundError as e:
            logger.warning("the json file not exist")
            return []

