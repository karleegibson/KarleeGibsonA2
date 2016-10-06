from item import Item


def main():
    item1 = Item("Watch", 24.60, 2, False)
    print(item1)
    item1.complete_item()
    print(item1.completed)
    print(item1)

main()
