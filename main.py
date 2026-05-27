import logging
from shape_manager import ShapeManager

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s" ,handlers=[logging.FileHandler("app.log",encoding="UTF-8")])
logger = logging.getLogger(__name__)

def add_shape(manager):
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


def show_all_shapes(manager):
    """
    
    """
    my_shapes = manager.get_all_shapes()
    for shape in my_shapes:
        print(shape.to_dict())

def update_shape(manager):
    """
    
    """
    choice_id = int(input("Enter the shape ID you want to update: "))
    my_shape = manager.find_shape_by_id(choice_id)

    if my_shape == "square":
        choice_change = {"side":float(input("Enter the new side: "))}

    if my_shape == "rectangle":
        choice_change = {"length" : float(input("Enter the new length: ")),"width" : float(input("Enter the new width: "))}

    if my_shape == "circle":
        choice_change = {"radius" : float(input("Enter the new radius: "))}
    
    manager.update_shape(choice_id , choice_change)

def delete_shape(manager):
    """
    
    """
    choice_id = int(input("Enter the shape ID you want to delete: "))
    manager.delete_shape(choice_id)

def menu():
    print("\n=== Shape CRUD Manager ===")
    print("1. Add shape")
    print("2. Show all shapes")
    print("3. Update shape")
    print("4. Delete shape")
    print("0. Exit")


def main():
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