class ItemList:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def add_items_from_list(self, items_as_lists):
        for item in items_as_lists:
            self.items.append(item)
            print(items)

    def get_items(self):
        item_list = []
        for item in self.items:
            item_list.append(item)
        return item_list

    def get_item_by_name(self):
        pass

    def add_item(self, item):
        self.products.append(item)

    def get_total_price(self):
        pass

    def sort_items(self):
        pass


        # for item in items_as_lists:
        # name = item[0]
        # price = item[1]
        # priority = item[2]
        # completed = item[3]
        # item = [name, price, priority, completed]
        # return item
