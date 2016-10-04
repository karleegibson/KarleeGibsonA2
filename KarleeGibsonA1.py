""" Name: Karlee Gibson
    Date: 28/08/16
    Brief program details:
                                            Shopping List 1.0
        Plan and code a console-based program in Python 3, using skills including selection, repetition,
        file input/output, exceptions, lists, functions and string formatting. The program is a simple shopping list
         which maintains a list of items in a file. The user can view required/completed items, add new items or mark
         items as completed.

    Link to GitHub: https://github.com/karleegibson/KarleeGibsonA1

Pseudocode:

function load_items()
    open "items.csv" as items_file for reading
    return a single list of all the lines from items_file and assign to items_in_text
    items = empty list
    for item in items_in_text
        item = strip item on whitespace and split item on commas
        item[1] = item[1] converted to float
        item[2] = item[2] converted to integer
        add item to items
    close items_file
    return items


function complete_an_item(required_items)
    total = 0
    for item in required_items
        total = total + 1
    display get item number message
    get item_number
    repeat while item_number not in range
        display invalid number message
        display get item number message
        get item_number
    item_to_complete = item with item_number from required_items list
    return item_to_complete



"""
import csv

MENU = "Menu: \nR - List required items \nC - List completed items \nA - Add new item \nM - Mark an item as " \
       "completed \nQ - Quit"


def main():
    """
        Shopping List program,
        maintain a list of items in a file based on user input, including displaying items, adding new items and
        marking items as complete
        """
    print("Shopping List 1.0 - by Karlee Gibson")
    list_of_items = load_items()
    print("{} items loaded from items.csv".format(len(list_of_items)))
    menu = choose_menu_option()
    while menu != "Q":

        if menu == "R":
            required_items = load_required_items(list_of_items)
            if required_items == []:
                print("No required items")
            else:
                print("Required items: ")
                count = 0
                for item in required_items:
                    print("{}. {:18} ${:6.2f} ({})".format(count, item[0], item[1], item[2]))
                    count += 1
                expected_price_of_items = calculate_expected_price(required_items)
                print("Total expected price for {} items: ${}".format(len(required_items), expected_price_of_items))
            menu = choose_menu_option()

        elif menu == "C":
            completed_items = load_completed_items(list_of_items)
            if completed_items == []:
                print("No completed items")
            else:
                print("Completed items: ")
                count = 0
                for item in completed_items:
                    print("{}. {:18} ${:6.2f} ({})".format(count, item[0], item[1], item[2]))
                    count += 1
                expected_price_of_completed_items = calculate_completed_expected_price(completed_items)
                print("Total expected price for {} items: ${}".format(len(completed_items),
                                                                      expected_price_of_completed_items))
            menu = choose_menu_option()

        elif menu == "A":
            new_item = add_new_item(list_of_items)
            menu = choose_menu_option()

        elif menu == "M":
            required_items = load_required_items(list_of_items)
            if required_items == []:
                print("No required items")
            else:
                print("Required items: ")
                count = 0
                for item in required_items:
                    print("{}. {:18} ${:6.2f} ({})".format(count, item[0], item[1], item[2]))
                    count += 1
                expected_price_of_items = calculate_expected_price(required_items)
                print("Total expected price for {} items: ${:.2f}".format(len(required_items), expected_price_of_items))
                item_to_be_completed = complete_an_item(required_items)
                print("{} marked as completed".format(item_to_be_completed[0]))
                if item_to_be_completed in list_of_items:
                    item_to_be_completed[3] = 'c'
            menu = choose_menu_option()

    updated_list = save_items(list_of_items)
    print("{} items saved to items.csv".format(len(list_of_items)))
    print("Have a nice day :)")


def choose_menu_option():
    """ get choice for menu options; return menu choice to the invoker menu in main"""
    print(MENU)
    try:
        menu_choice = input(">>>").upper()
        while menu_choice not in ['R', 'C', 'A', 'M', 'Q']:
            print("Invalid menu choice")
            print(MENU)
            menu_choice = input(">>>").upper()
        return menu_choice
    except ValueError:
        print("Invalid menu choice")
        print(MENU)


def load_items():
    """ open and items.csv; read and return a single list of all the lines from the file; add each item to items list
    and return items to the invoker list_of_items in main; close csv file"""
    items_file = open('items.csv', 'r')
    items_in_text = items_file.readlines()
    items = []
    for item in items_in_text:
        item = item.strip().split(',')
        item[1] = float(item[1])  # change type from string to float
        item[2] = int(item[2])
        items.append(item)
    items_file.close()
    return items


def load_required_items(list_of_items):
    """ add each required item to required items list from list_of_items; return required items list to the invoker
    required_items in main """
    required_items_list = []
    for item in list_of_items:
        if item[3] == 'r':
            required_items_list.append(item)
    return required_items_list


def load_completed_items(list_of_items):
    """ add each completed item from list_of_items to completed items list; return completed items list to the
        invoker completed_items in main """
    completed_items_list = []
    for item in list_of_items:
        if item[3] == 'c':
            completed_items_list.append(item)
    return completed_items_list


def calculate_expected_price(required_items):
    """ calculate expected price based on item costs in required items list; return expected price to the invoker
    expected_price_of_items in main """
    expected_price = 0.00
    for item in required_items:
        expected_price += item[1]
    return expected_price


def calculate_completed_expected_price(completed_items):
    """ calculate expected price based on item costs in completed items list; return expected price to the invoker
    expected_price_of__completed_items in main """
    expected_price = 0.00
    for item in completed_items:
        expected_price += item[1]
    return expected_price


def add_new_item(list_of_items):
    """ add a new item to list_of_items based on inputs; use exceptions for error handling; print new item added message
    and return list of items to the invoker new_items in main """
    item_name = str(input("Item name: "))
    while item_name == "":
        print("Input can not be blank")
        item_name = input("Item name: ")
    valid_input = False
    while not valid_input:
        try:
            item_price = float(input("Price: $"))
            while item_price < 0:
                print("Price must be >= $0")
                item_price = float(input("Price: $"))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
            valid_input = False
    valid_input = False
    while not valid_input:
        try:
            item_priority = int(input("Priority: "))
            while item_priority not in (1, 2, 3):
                print("Priority must be 1, 2 or 3")
                item_priority = int(input("Priority: "))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
            valid_input = False
    completion = 'r'
    print("{}, ${:.2f} (priority {}) added to shopping list".format(item_name, item_price, item_priority))
    list_of_items.append([item_name, item_price, item_priority, completion])
    return list_of_items


def complete_an_item(required_items):
    """ mark an item as completed based on input; return item to complete to the invoker item_to_be_completed in main
    """
    # count number of items in required_items list, use as range for user input for item_number
    total = 0
    for item in required_items:
        total += 1
    print("Enter the number of an item to mark as completed")
    valid_input = False
    while not valid_input:
        try:
            item_number = int(input(">>>"))
            while item_number not in range(0, total):
                print("Invalid item number")
                item_number = int(input(">>>"))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a number")
            valid_input = False
    item_to_complete = required_items[item_number]
    return item_to_complete


def save_items(list_of_items):
    """ open and items.csv; write each item in list_of_items to items.csv, for the purpose of overwriting original
    content; close csv file """
    items_file = open('items.csv', 'w')
    items_writer = csv.writer(items_file)
    for item in list_of_items:
        items_writer.writerow(item)
    items_file.close()


main()
