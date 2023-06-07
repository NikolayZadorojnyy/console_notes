from typing import List
from datetime import datetime
from note import *
import csv


class Model:

    def __init__(self, notes: list):
        self.notes = notes

    def create_note(self):
        cur_title = input("Введите заголовок заметки: ")
        cur_content = input("Введите содержимое заметки: ")
        if not self.notes:
            note = Note(id=1, title=cur_title, content=cur_content)
        else:
            note = Note(id=(len(self.notes) + 1),
                        title=cur_title, content=cur_content)
        self.notes.append(note)
        print("Заметка успешно создана!")

    def delete_note(self):
        for note in self.notes:
            print(f"Записка №{note.id}, {note.title}\n")
        u_choice = input("Выберите по id записку, которую хотите удалить:")
        self.notes.remove(u_choice)
        print("Записка успешно удалена!")

    def find_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                found_note = note
        return found_note

    def show_note_by_id(self):
        choice_id = input("Введите id искомой записки: ")
        for note in self.notes:
            if note.id == choice_id:
                print(f"Искомая записка:\n{note}")

    def edit_note(self):
        for note in self.notes:
            print(f"Записка №{note.id}, {note.title}")
        choice_note = input(
            "Выберите по id записку, которую хотите отредактировать:")
        edit_note = Model.find_note_by_id(self, choice_note)
        print("Что вы хотите в ней отредактировать?")
        print("1 - title;\n2 - content")
        choice_item = input("Введите номер желаемого пункта: ")
        match choice_item:
            case "1":
                choice_edit_item = input(
                    "Введите новое название заголовка заметки: ")
                edit_note.title = choice_edit_item
                print("Заголовок записки успешно отредактирован!")
            case "2":
                choice_edit_item = input("Введите новое содержимое заметки: ")
                edit_note.content = choice_edit_item
                print("Содержимое записки успешно отредактировано!")
            case _:
                print("Такого пункта нет!")

    def save_to_file(self):
        # save_choice = input("Сохранить данный в файл csv?\n1 - да\n2 - нет\n")
        # match save_choice:
        #     case "1":
        with open("notes.csv", "w") as csv_wr:
            writer = csv.writer(csv_wr)
            for note in self.notes:
                writer.writerow(note)