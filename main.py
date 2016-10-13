""" Name: Karlee Gibson
    Date: 28/08/16
    Brief program details:
                                            Shopping List 2.0
        Plan

    Link to GitHub:

"""

from KarleeGibsonA1 import load_items, save_items
from item import Item
from itemlist import ItemList
from kivy.app import App
from kivy.lang import Builder

import csv


class ShoppingList(App):
    def build(self):
        self.title = "Shopping List 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root

        items_as_lists = load_items()
        items_as_lists


# create and start the App running
ShoppingList().run()
