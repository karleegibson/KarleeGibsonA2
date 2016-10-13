from item import Item


class ItemList:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str([str(item) for item in self.items])

    def add_items_from_list(self, items_as_lists):
        for item in items_as_lists:
            self.items.append(Item(item[0], item[1], item[2], item[3]))

    def get_items(self):
        pass

    def get_item_by_name(self, name):
        # return self.items[0]
        for item in self.items:
            if item.name == name:
                return item

    def add_item(self, item):
        pass

    def get_total_price(self):
        pass

    def sort_items(self):
        pass

