from View import View
from Model import Model
import os


class Controller:
    def __init__(self):
        self.__view = None
        self.__model = Model()
        self.__picked_file = None

    def set_view(self, view):
        self.__view = view

    def file_ask(self):
        option = self.__view.show_folder()
        if option:
            file_name = os.path.basename(option)  # converts the full file path to just its name
            self.__picked_file = file_name
            self.__view.change_send_btn(True)  # Makes the send button clickable
            self.__view.notifications("Valitud fail: " + file_name)  # Displays which file is selected
            self.__model.selected_file = option  # sets the "selected_file" variable in model to the file path

    def search_click(self, search_str):
        if len(search_str) > 2:  # makes sure the search text is longer than 2 characters
            answer = self.__model.search_file(search_str)
            if not answer:
                self.__view.create_messagebox("Vastust ei leitud", "Sisestatud otsingufraas ei olnud valitud failis.")
            else:
                if self.__picked_file == "Persons_Big.csv":
                    self.__view.generate_large_table(answer)
                else:
                    self.__view.generate_table(answer)
        else:
            self.__view.create_messagebox("Vastust ei leitud",
                                          "Sisetatud otsingufraas peab olema pikkem kui kaks tähemärki.")
