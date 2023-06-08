from view import *
from model import *


class Presenter():

    def __init__(self, model_obj: Model, view_obj: View):
        self.model = model_obj
        self.view = view_obj

    def start(self):
        flag = False
        while (not flag):
            menu_choice = self.view.print_menu()
            if menu_choice == "1":
                self.model.show_notes()
            elif menu_choice == "2":
                self.model.show_note_by_id()
            elif menu_choice == "3":
                self.model.create_note()
            elif menu_choice == "4":
                self.model.edit_note()
            elif menu_choice == "5":
                self.model.delete_note()
            elif menu_choice == "6":
                self.model.save_data()
            elif menu_choice == "7":
                self.model.load_data()
            elif menu_choice == "8":
                print("--Программа завершена--")
                flag = True
            else :
                print("Такого пункта нет!\n")