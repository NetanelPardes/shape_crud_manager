import logging
from shape_manager import ShapeManager

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s" ,handlers=[logging.FileHandler("app.log",encoding="UTF-8")])
logger = logging.getLogger(__name__)

def add_shape(manager):
    """
    A function that prints to the user what shape they want to add
    and invokes the create_shape function of the ShapeManager class with the correct variable.
    """
    print("\n===new shape===")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    
    shape_choice = input("Enter your choice: ")

    id = manager.get_id()

    try:
        if shape_choice == '1':
            side = float(input("Enter the side of the square: "))
            manager.create_shape({"shape_id":id, "shape_type": "square","side" : side})
        
        elif shape_choice == '2':
            length = float(input("Enter the length of the Rectangle: "))
            width = float(input("Enter the width of the Rectangle: "))
            manager.create_shape({"shape_id":id ,"shape_type": "rectangle","length" : length ,"width" : width})

        elif shape_choice == '3':
            radius = float(input("Enter the radius of the Circle: "))
            manager.create_shape({"shape_id":id,"shape_type": "circle","radius" : radius})
        else:
            print("Wrong choice!")

    except ValueError as e:
        print(f"{e} : Negative numbers are not allowed.")
        logger.info("The user typed negative numbers into a shape.")
    except TypeError as e:
        print(f"You need to enter a number.")
        logger.warning("The user entered something other than a number.")


def show_all_shapes(manager):
    """
    A function receives the entire list of shapes and prints each one.
    """
    my_shapes = manager.get_all_shapes()
    for shape in my_shapes:
        print(shape.to_dict())


def update_shape(manager):
    """
    A function that receives the shape number
    checks its type and sends it to the update_shape function of the ShapeManager class.
    """
    try:
        choice_id = int(input("Enter the shape ID you want to update: "))
        my_shape = manager.find_shape_by_id(choice_id)

        if my_shape == "square":
            choice_change = {"side":float(input("Enter the new side: "))}

        elif my_shape == "rectangle":
            choice_change = {"length" : float(input("Enter the new length: ")),"width" : float(input("Enter the new width: "))}

        elif my_shape == "circle":
            choice_change = {"radius" : float(input("Enter the new radius: "))}

        else:
            print("Shape ID not found.")
            return
        
        manager.update_shape(choice_id , choice_change)
    except KeyError as e:
        print("Shape ID not found.")
    except ValueError as e:
        print(f"{e} : Negative numbers are not allowed.")
        logger.info("The user typed negative numbers into a shape.")
    except TypeError as e:
        print(f"You need to enter a number.")
        logger.warning("The user entered something other than a number.")


def delete_shape(manager):
    """
    A function that receives the shape number and sends it to the delete_shape function of the ShapeManager class 
    which deletes the object from the file.
    """
    try:    
        choice_id = int(input("Enter the shape ID you want to delete: "))
        manager.delete_shape(choice_id)

    except KeyError as e:
        print("Shape ID not found.")
    except ValueError as e:
        print(f"{e} : Negative numbers are not allowed.")
        logger.info("The user typed negative numbers into a shape.")
    except TypeError as e:
        print(f"You need to enter a number.")
        logger.warning("The user entered something other than a number.")


def menu():
    """
    Function that prints the system menu
    """
    print("\n=== Shape CRUD Manager ===")
    print("1. Add shape")
    print("2. Show all shapes")
    print("3. Update shape")
    print("4. Delete shape")
    print("0. Exit")


def main():
    """
    Main function
    """
    logging.info("The program started working.")
    
    manager = ShapeManager()

    while True:
        menu()
        choice = input("Enter your choice: ")
    
        if choice == "1":
            add_shape(manager)

        elif choice == "2":
            show_all_shapes(manager)

        elif choice == "3":
            update_shape(manager)
            

        elif choice == "4":
            delete_shape(manager)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()
