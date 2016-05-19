"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""

shopping_list = []

def menu():
    choice = int(raw_input("Choose from the following options: \n" 
                       "0 - Main Menu \n"
                       "1 - Show current list. \n"
                       "2 - Add an item to your shopping list.\n"
                       "3 - Remove an item\n"
                       "4 - Replace an item\n"))
    if choice == 0:
        menu()
    elif choice == 1:
        sorted_shopping_list()
    elif choice == 2:
        item = raw_input("Add an item: ")
        add_shopping_list(item)
    elif choice == 3:
        item = raw_input("Remove an item: ")
        remove_item(item)
    elif choice == 4:
        old_item = raw_input("Replace this item: ")
        new_item = raw_input("Replace it with: ")
        replace_item(old_item, new_item)
    else:
        print "That is not an option"

def main():
    while (True):
        menu()
        item = raw_input("M - Main Menu\nE - Exit")
        if item == "E":
            break
        elif item == "M":
            menu()
        else:
            print "Nope. Try again."
    print "Your items are", shopping_list

def add_shopping_list(item):
    item = item.lower()
    item_list = []
    if "," in item:
        item_list.extend(split_string(item))
    else:
        item_list.append(item)
        
    for itm in item_list:
            if itm not in shopping_list:
                shopping_list.append(itm)
                print "Here's your updated list", sorted_shopping_list()
            else:
                print "This item %s already exists!" % (itm)


def sorted_shopping_list():
    if shopping_list:
        shopping_list.sort()
        print shopping_list
        return shopping_list
    else:
        print "Your list is empty"

def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list()
    else:
        print "%s was not on the list." % (item)


def replace_item(old_item, new_item):
    old_item = old_item.lower()
    new_item = new_item.lower()

    if old_item in shopping_list:
        item_index = shopping_list.index(old_item)
        shopping_list[item_index] = new_item
        print "%s has replaced %s in the list." % (new_item, old_item)
    else:
        print "%s is not in the list." % (old_item)


def split_string(item):
    temp_list = []
    split_items = list(item.split(", "))
    for sp_item in split_items:
         temp_list.append(sp_item)
    return temp_list

# # TEST FUNCTIONS
# # 1 - add 4 times to your shopping list
# add_shopping_list("apple")
# add_shopping_list("steak")
# add_shopping_list("beef")
# add_shopping_list("mustard")

# # 2 - Add an item that is already in the list. what happens?
# add_shopping_list("apple")

# # 3 - Remove an item on your list
# remove_item("apple")

# # 4 - Remove an item that is not in the list. what happens?
# remove_item("chicken")

# # 5 - you've changed your mind on one of your items. you want to substitute it with something else.
# replace_item("mustard", "ketchup")


if __name__ == '__main__':
    main()



