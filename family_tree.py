root = {"name": "brown", "hair": "brown", "children": [{'name': 'john', 'hair': 'brown'}, {'name': 'lisa', 'hair': 'red'}]}
def print_children(person):
    if person["children"]:
        # will refactor the line below to print each child out
        print("Children: ", person["children"])
    else:
        # Prints the text below only to show that the node has no children
        print("Children: ")

def check_dupicate_child(array, child_name):
    for child in array:
        if child["name"] == child_name:
            return True

def display_person(person):
    print("Name: ", person["name"])
    print("Hair: ", person["hair"])
    print_children(person)

def ask_for_child(root):
    current_person = root
    child_name = input("Please enter the child's name (or 'return' or 'exit'... ")
    if child_name == "exit":
        print("exiting")
        quit()
        print("this should not display")
    elif child_name == "return":
        print("returning")
        display_person(current_person)
        ask_for_child()
    elif check_dupicate_child(current_person["children"], child_name):
        print("this child name exists")
        current_person = current_person["children"]["name"]
        ask_for_child(current_person)
    else:
        name = child_name
        hair = input("Hair color?...")
        new_child = {"name": name, "hair": hair}
        current_person["children"].append(new_child)
        display_person(current_person)
        ask_for_child(current_person)

current_person = root
display_person(current_person)
ask_for_child(current_person)
    

