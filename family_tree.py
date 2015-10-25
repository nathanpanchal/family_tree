root = {"name": "Bob", "hair": "Brown", "children": ["John", "Guys"]}
def print_children(person):
    if person["children"]:
        print("Children: ", person["children"])
    else:
        print("Children: ")

def display_person(person):
    print("Name: ", person["name"])
    print("Hair: ", person["hair"])

def ask_for_child():
    child_name = input("Please enter the child's name (or 'return' or 'exit'... ")
    return child_name

current_person = root
child_name = ask_for_child()
if child_name == "exit":
    print("exiting")
    quit()
    print("this should not display")
#     exit the program
elif child_name == "return":
    print("returning")
    display_person(current_person)
#     print the previous person and ask for child name
else:
    name = child_name
    hair = input("Hair color?...")
    new_child = {"name": name, "hair": hair}
    current_person["children"].append(new_child)
    display_person(current_person)
    

