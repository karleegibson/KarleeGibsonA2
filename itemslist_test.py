from itemlist import ItemList
from item import Item
from KarleeGibsonA1 import load_items, save_items


def main():
    items_as_lists = load_items()
    print(items_as_lists)
    items = ItemList()
    items.add_items_from_list(items_as_lists)
    print(items)

    # items.add_items_from_list(items_as_lists)
    # print(items)

    # item = Item("Soap", 12.95, 3, False)
    # items.add_item(item)
    # print(item)
    # print(items)

main()
