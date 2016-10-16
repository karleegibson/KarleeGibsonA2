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
from kivy.properties import StringProperty

import csv


class ShoppingListApp(App):
    """ Main program - Kivy app to demo dynamic widget creation """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.item_list = load_items()

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Shopping List 2.0"
        self.root = Builder.load_file('app.kv')
        # self.create_widgets()
        return self.root

    # def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        # for item in self.item_list:
            # create a button for each phonebook entry
            # temp_button = Button(text=item)
            # temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            # self.root.ids.entriesBox.add_widget(temp_button)

    # def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        # item = instance.text
        # self.status_text = "{}'s number is {}".format(item, self.item_list[item])

    # def clear_all(self):
        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """
        # self.root.ids.entriesBox.clear_widgets()


ShoppingListApp().run()
