from item import Item
from operator import attrgetter


class ItemList:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str([str(item) for item in self.items])

    def add_items_from_list(self, items_as_lists):
        """
        Convert list of lists to a list of Item objects
        :param items_as_lists:
        :return: None
        """
        for item in items_as_lists:
            self.items.append(Item(item[0], item[1], item[2], item[3]))

    def get_items(self):
        """
        Convert the Item objects to a list of lists
        :return: list of lists to be used by csv saving code
        """
        items_as_lists = []
        for item in self.items:
            items_as_lists.append([item.name, item.price, item.priority, item.completed])
        return items_as_lists

    def get_item_by_name(self, name):
        """
        Take in a name and return Item object with that name
        :param name
        :return: Item object
        """
        for item in self.items:
            if item.name == name:
                return item

    def add_item(self, name, price, priority):
        """
        Add a single Item object to the items list attribute
        :param name:
        :param price:
        :param priority:
        :return: None
        """
        completed = 'r'
        new_item = [name, price, priority, completed]
        self.items.append(Item(new_item[0], new_item[1], new_item[2], new_item[3]))

    def get_total_price(self):
        """
        Calculate total price of items in items list attribute
        :return: total price
        """
        total_price = 0
        for item in self.items:
            if item.completed == 'r':
                total_price += item.price
        return "Total price: ${:.2f}".format(total_price)

    def sort_items(self):
        self.items.sort(key=attrgetter("priority"))

