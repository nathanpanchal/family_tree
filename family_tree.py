root = {"name": "bob", "hair": "brown", "children": [{"name": "Jane"}, {"name": "David"}]}

# makes sure that if the list of children is blank the correct string is displayed
def print_children(person):
    if person["children"]:
        for child in person["children"]:
            print(" " + child["name"])
    else:
        print("Children: ")

def check_child_exists(array, child_name):
    for child in array:
        if child["name"] == child_name:
            return True

def display_person(person):
    print("Name: ", person["name"])
    print("Hair color: ", person["hair"])
    print_children(person)

def prompt():
    name = input('Enter a child\'s name, or \"return\", or \"exit\":')
    return name

current_person = root
display_person(current_person)
prompt()
while True
    display_person(current_person)
    choice = prompt
