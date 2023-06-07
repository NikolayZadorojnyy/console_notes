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
            match menu_choice:
                case "1":
                    self.model.show_notes()
                case "2":
                    self.model.show_note_by_id()
                case "3":
                    self.model.create_note()
                case "4":
                    self.model.edit_note()
                case "5":
                    self.model.delete_note()
                case "6":
                    self.model.save_data()
                case "7":
                    self.model.load_data()
                case "8":
                    print("Произведен выход из заметок.")
                    flag = True