""" Name: Karlee Gibson
    Date: 28/08/16
    Brief program details:
                                            Shopping List 2.0
        Create a Graphical User Interface (GUI) version of the program made in assignment 1, using Python 3 and the
        Kivy toolkit. The program will help build skills on using classes and GUIs as well as incorporating the skills
        used in assignment 1 like selection, repetition, exceptions, lists and functions. The program will reuse some
        of the code in assignment one.

    Link to GitHub:

    Link to GitHub original repository which includes all commits: https://github.com/karleegibson/KarleeGibsonA2
        24 commits
        Was not able to transfer these commits to classroom repository, only files

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
    """ Main program - Shopping List App"""
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
        self.root.ids.priceOrCompletedLabel.text = self.item_list.get_total_price()
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
        """
        Handler for user pressing list required button
        :return: None
        """
        self.root.ids.entriesBox.clear_widgets()
        self.root.ids.priceOrCompletedLabel.text = self.item_list.get_total_price()

        for item in self.item_list.items:
            if item.completed == 'r':
                # create a button for each item entry
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.complete_an_item)
                if item.priority == 1:
                    temp_button.background_color = (255, 0, 0, 0.7)
                elif item.priority == 2:
                    temp_button.background_color = (0, 0, 255, 0.7)
                else:
                    temp_button.background_color = (0, 128, 0, 0.7)
                    # add the button to the "entriesBox" using add_widget()
                self.root.ids.entriesBox.add_widget(temp_button)

    def display_completed_items(self):
        """
        Handler for user pressing list completed button
        :return: None
        """
        self.root.ids.priceOrCompletedLabel.text = 'Showing completed items'
        self.root.ids.entriesBox.clear_widgets()

        for item in self.item_list.items:
            if item.completed == 'c':
                # create a button for each item entry
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.get_item_information)
                self.root.ids.entriesBox.add_widget(temp_button)

    def get_item_information(self, instance):
        """
        Handler for pressing entry buttons in completed items list
        :param instance: the Kivy button instance
        :return: None
        """
        item_name = instance.text
        item_name = self.item_list.get_item_by_name(item_name)
        self.root.ids.statusLabel.text = str(item_name)

    def complete_an_item(self, instance):
        """
        Handler for pressing entry buttons in required items list
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        item = instance.text
        self.root.ids.entriesBox.remove_widget(instance)
        item = self.item_list.get_item_by_name(item)
        item.complete_item()
        self.root.ids.priceOrCompletedLabel.text = self.item_list.get_total_price()
        self.root.ids.statusLabel.text = 'Completed: {}'.format(item)

    def add_new_item(self):
        """
        Handles user input for adding a new item and adds new item to item list
        :return: None
        """
        name = self.root.ids.nameTextInput.text
        price = self.root.ids.priceTextInput.text
        priority = self.root.ids.priorityTextInput.text

        if name == '' or price == '' or priority == '':
            self.root.ids.statusLabel.text = 'All fields must be completed'
            return
        try:
            price = float(price)
            if price < 0:
                self.root.ids.statusLabel.text = 'Price must not be negative'
                return
        except ValueError:
            self.root.ids.statusLabel.text = 'Please enter a valid number'
            return
        try:
            priority = int(priority)
            if priority not in (1, 2, 3):
                self.root.ids.statusLabel.text = 'Priority must be 1, 2 or 3'
                return
        except ValueError:
            self.root.ids.statusLabel.text = 'Please enter a valid number'
            return

        self.item_list.add_item(name, price, priority)
        self.item_list.sort_items()
        temp_button = Button(text=name)
        temp_button.bind(on_release=self.complete_an_item)

        if priority == 1:
            temp_button.background_color = (255, 0, 0, 0.7)
        elif priority == 2:
            temp_button.background_color = (0, 0, 255, 0.7)
        else:
            temp_button.background_color = (0, 128, 0, 0.7)
        self.root.ids.entriesBox.add_widget(temp_button)

        self.root.ids.nameTextInput.text = ''
        self.root.ids.priceTextInput.text = ''
        self.root.ids.priorityTextInput.text = ''

    def clear_text(self):
        """
        Clears text in adding new item text inputs when clear button is pressed
        :return: None
        """
        self.root.ids.nameTextInput.text = ''
        self.root.ids.priceTextInput.text = ''
        self.root.ids.priorityTextInput.text = ''

    def on_stop(self):
        """
        Gets and saves list of item lists to items.csv when user closes Shopping List app
        :return: None
        """
        list_of_item_lists = self.item_list.get_items()
        save_items(list_of_item_lists)


ShoppingListApp().run()
