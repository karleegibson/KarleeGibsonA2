class Item:
    def __init__(self, name, price, priority, completed):
        self.name = name
        self.price = price
        self.priority = priority
        self.completed = completed

    def __str__(self):
        completed = ''
        if self.completed:
            completed = '(completed)'
        return "{}, ${:.2f}, priority {} {}".format(self.name, self.price, self.priority, completed)

    def complete_item(self):
        self.completed = True

