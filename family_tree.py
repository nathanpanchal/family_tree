def print_children(person):
    if person["children"]:
        for child in person["children"]:
            print(" " + child["name"].capitalize())
    else:
        print("Children: ")

root = {"name": "bob",
        "hair": "brown",
        "children": []}
current_node = root
while True:
    print("Name: ", current_node["name"].capitalize())
    print("Hair color: ", current_node["hair"].capitalize())
    print_children(current_node)
    choice = input(
        'Enter a child\'s name, or \"return\", or \"exit\":'
        ).lower()
    if choice == "exit":
        break
    elif choice == "return":
        current_node = root
        continue
    else:
        for child in current_node["children"]:
            if child["name"] == choice:
                current_node = child
                break
        else:
            hair = input(
                "What is {0}\'s hair color?".format(choice.capitalize())
                ).lower()
            new_child = {"name": choice, "hair": hair, "children": []}
            current_node["children"].append(new_child)
            current_node = new_child
