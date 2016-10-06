from itemlist import ItemList
from KarleeGibsonA1 import load_items, save_items


def main():
    items_as_lists = load_items()
    # print(items_as_lists)
    items = ItemList()
    print(items)
    items.add_items_from_list(items_as_lists)
    print(items)

main()
