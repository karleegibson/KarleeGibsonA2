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
from kivy.uix.button import Button
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
        self.items_as_lists = load_items()
        self.item_list = ItemList()
        self.item_list.add_items_from_list(self.items_as_lists)
        self.item_list.sort_items()

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Shopping List 2.0"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        self.root.ids.priceOfCompletedLabel.text = self.item_list.get_total_price()
        self.root.ids.statusLabel.text = 'Click items to mark them as completed'
        return self.root

    def create_widgets(self):
        """
        Create buttons from list of items and add them to the GUI
        :return: None
        """
        for item in self.item_list.items:
            if item.completed == 'r':
                # create a button for each item entry
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.complete_an_item)
                if item.priority == 1:
                    temp_button.background_color = (255, 0, 0, 0.7)  # change these values to be in between 0 and 1
                elif item.priority == 2:
                    temp_button.background_color = (0, 0, 255, 0.7)
                else:
                    temp_button.background_color = (0, 128, 0, 0.7)
                    # add the button to the "entriesBox" using add_widget()
                self.root.ids.entriesBox.add_widget(temp_button)

    def display_required_items(self):
        self.root.ids.entriesBox.clear_widgets()

        for item in self.item_list.items:
            if item.completed == 'r':
                # create a button for each item entry
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.complete_an_item)
                if item.priority == 1:
                    temp_button.background_color = (255, 0, 0, 0.7)  # change these values to be in between 0 and 1
                elif item.priority == 2:
                    temp_button.background_color = (0, 0, 255, 0.7)
                else:
                    temp_button.background_color = (0, 128, 0, 0.7)
                    # add the button to the "entriesBox" using add_widget()
                self.root.ids.entriesBox.add_widget(temp_button)

    def display_completed_items(self):
        self.root.ids.priceOfCompletedLabel.text = 'Showing completed items'
        self.root.ids.entriesBox.clear_widgets()

        for item in self.item_list.items:
            if item.completed == 'c':
                # create a button for each item entry
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.complete_an_item) # change to method that displays item info
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entriesBox.add_widget(temp_button)

        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """

    def complete_an_item(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        item = instance.text
        self.root.ids.entriesBox.remove_widget(instance)
        item = self.item_list.get_item_by_name(item)
        item.complete_item()
        print(item)
        self.root.ids.priceOfCompletedLabel.text = self.item_list.get_total_price()
        self.root.ids.statusLabel.text = 'Completed: {}'.format(item)

    def add_new_item(self):
        pass




ShoppingListApp().run()
