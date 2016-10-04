class Item:
    def __init__(self, name, price, priority):
        self.name = name
        self.price = price
        self.priority = priority

    def __str__(self):
        return "{}, ${:.2f}, priority {} (completed)".format(self.name, self.price, self.priority)

    def complete_item(self):
        self.priority = "completed"
