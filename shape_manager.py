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
        A function that receives a dictionary of data and creates a form from it according to its class
        It is used both to create a new form and to load the information from a file
        """
        try:
            if shape_dict["shape_type"] == "square":
                my_shape = Square(shape_dict["shape_id"],shape_dict["side"])
            
            elif shape_dict["shape_type"] == "rectangle":
                my_shape = Rectangle(shape_dict["shape_id"], shape_dict["length"] , shape_dict["width"])
            
            elif shape_dict["shape_type"] == "circle":
                my_shape = Circle(shape_dict["shape_id"],shape_dict["radius"])
            
            self.shapes.append(my_shape)
            self.save_to_json()
        
        except KeyError as e:
            print("Missing required field")
        
    
    def get_all_shapes(self):
        """
        A function that returns a list of all shapes
        Used to print the shapes
        """
        return self.shapes

    
    def update_shape(self, shape_id, new_data):
        """
        A function that updates one of the shapes
        It gets the shape's data from the sort
        It updates the shape in the shape list and loads the list back into the file
        """
        for val in new_data.values():
            if val <= 0:
                raise ValueError("You cannot enter negative numbers.")
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
                print("The shape was updated successfully.")
                logger.info("The shape %s (%s) was updated successfully With the data %s." , shape_id,shape.shape_type ,new_data)
                return
        raise KeyError("The key does not exist in the system.")
        
        
    def delete_shape(self, shape_id):
        """
        A function that takes the shape that needs to be deleted
        removes it from the list of shapes
        and loads the list back into the file        
        """
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                print("The shape was Deleted successfully.")
                logger.info("The shape %s (%s) was Deleted successfully." , shape_id,shape.shape_type)
                return

        raise KeyError("The key does not exist in the system.")        

    
    def save_to_json(self):
        """
        A function loads the list of shapes into a json file
        """
        try:
            with open("shapes.json", "w", encoding="utf-8") as file:
                logger.info("The %s file is opened for writing information." , file.name)
                json.dump([shape.to_dict() for shape in self.shapes], file, indent=4)
                logger.info("The list %s was saved to a file." , self.shapes)
        
        except OSError as e:
            print(f"Could not write to JSON file: {e}")
            logger.warning("You do not have permission to access the file %s.", file.name)
    
    
    def find_shape_by_id(self, shape_id):
        """
        A function that receives the shape number and returns its type according to what is in the list
        If the number is not in the list it will return None
        """
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                return shape.shape_type
        return None


    def get_id(self):
        """
        A function that returns the highest shape number in the file, plus one
        Use it to get a new id to create a shape
        """
        if not self.shapes:
            return 1
        return max(shape.shape_id for shape in self.shapes) + 1
        

    def load_from_json(self):
        """
        A function loads the contents of a json file,
        and automatically loads the contents into a list of shapes using the create_shape function
        The function will return an error if the file does not exist or the file was not opened properly
        """
        try:
            with open("shapes.json", "r", encoding="utf-8") as file:

                logger.info("The file %s is opened to read information." , file.name)
                shapes_data = json.load(file)
                
                for shape in shapes_data:
                    self.create_shape(shape)
                logger.info("The list %s was loaded from the file" , self.shapes)
        
        except FileNotFoundError as e:
            print("the json file not exist")
            logger.warning("the json file not exist")
            return []
        except json.JSONDecodeError as e:
            print("There was a problem opening the file.")
            logger.warning("There was a problem opening the file.")

if __name__ == "__main__":
    print("=== ShapeManager tests ===")

    manager = ShapeManager()

    manager.create_shape({
        "shape_id": 100,
        "shape_type": "square",
        "side": 5
    })

    manager.create_shape({
        "shape_id": 101,
        "shape_type": "rectangle",
        "length": 4,
        "width": 6
    })

    manager.create_shape({
        "shape_id": 102,
        "shape_type": "circle",
        "radius": 3
    })

    print("All shapes:")
    for shape in manager.get_all_shapes():
        print(shape.to_dict())

    print("Find shape 100:")
    print(manager.find_shape_by_id(100))

    print("Update shape 100:")
    manager.update_shape(100, {"side": 8})

    print("Delete shape 101:")
    manager.delete_shape(101)

    print("All shapes after update and delete:")
    for shape in manager.get_all_shapes():
        print(shape.to_dict())

    try:
        manager.update_shape(999, {"side": 5})
    except KeyError as e:
        print("Error:", e)

    try:
        manager.delete_shape(999)
    except KeyError as e:
        print("Error:", e)