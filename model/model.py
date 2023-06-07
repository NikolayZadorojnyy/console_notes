from typing import List
from note import *
from datetime import datetime


class Model:

    def __init__(self, notes: List[Note]):
        self.notes = notes

    def create_note(self):
        cur_title = input("Введите заголовок заметки: ")
        cur_content = input("Введите содержимое заметки: ")
        if not self.notes:
            note = Note(id=1, title=cur_title,
                        content=cur_content, date=datetime.now())
        else:
            note = Note(id=(len(self.notes) + 1), title=cur_title,
                        content=cur_content, date=datetime.now())
        self.notes.append(note)
        print("Заметка успешно создана!")

    def delete_note(self):
        u_choice = input("Выберите по id записку, которую хотите удалить:")
        for note in self.notes:
            print(f"Записка №{note.id}, {note.title}\n")
        self.notes.remove(u_choice)
        print("Записка успешно удалена!")

    def edit_note(self):
        for note in self.notes:
            print(f"Записка №{note.id}, {note.title}\n")
        choice_note = input(
            "Выберите по id записку, которую хотите отредактировать: ")
        edit_note = Model.find_note_by_id(self, choice_note)
        print("Что вы хотите в ней отредактировать?")
        print("1 - title;\n2 - content")
        choice_item = input("Введите номер желаемого пункта: ")
        if choice_item == "1":
            choice_edit_item = input(
                "Введите новое название заголовка заметки: ")
            edit_note.title = choice_edit_item
            print("Заголовок записки успешно отредактирован!\n")
        elif choice_item == "2":
            choice_edit_item = input("Введите новое содержимое заметки: ")
            edit_note.content = choice_edit_item
            print("Содержимое записки успешно отредактировано!\n")
        else:
            print("Такого пункта нет!\n")