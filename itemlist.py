class ItemList:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def add_items_from_list(self, items_as_lists):
        for item in items_as_lists:
            self.items.append(item)

    def get_items(self):
        pass

    def get_item_by_name(self):
        pass

    def add_item(self, item):
        pass

    def get_total_price(self):
        pass

    def sort_items(self):
        pass
