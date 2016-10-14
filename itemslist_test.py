from itemlist import ItemList
from item import Item
from KarleeGibsonA1 import load_items, save_items


def main():
    items_as_lists = load_items()
    # print(items_as_lists)

    # items = ItemList()
    # items.add_items_from_list(items_as_lists)
    # print(items)

    # items.add_items_from_list(items_as_lists)
    # print(items)

    # item = Item("Soap", 12.95, 3, False)
    # items.add_item(item)
    # print(item)
    # print(items)

    item_list = ItemList()
    print(item_list)
    item_list.add_items_from_list(items_as_lists)
    print(item_list)

    print(item_list.get_item_by_name('Fish fingers'))

    print(item_list.get_items())

    item_list.add_item('Watch', 12.95, 2)
    print(item_list)

    print(item_list.get_items())

    print(item_list.get_total_price())

    item_list.sort_items()
    print(item_list)

main()
