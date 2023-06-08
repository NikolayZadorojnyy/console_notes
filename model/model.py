from note import *
import csv


class Model:

    def __init__(self, notes: list):
        self.notes = notes

    def show_notes(self):
        print("Список заметок:")
        new_notes = Model.sort_by_date(self)
        for note in new_notes:
            print(f"{note}\n")

    def create_note(self):
        cur_title = input("Введите заголовок заметки: ")
        cur_content = input("Введите содержимое заметки: ")
        if not self.notes:
            note = Note(id="1", title=cur_title, content=cur_content)
        else:
            note = Note(id=str((len(self.notes) + 1)),
                        title=cur_title, content=cur_content)
        self.notes.append(note)
        print("Заметка успешно создана!\n")

    def delete_note(self):
        for note in self.notes:
            print(f"Записка №{note.id}, {note.title}\n")
        u_choice = input("Выберите по id записку, которую хотите удалить:")
        self.notes.remove(Model.find_note_by_id(self, u_choice))
        print("Записка успешно удалена!\n")

    def find_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                found_note = note
            return found_note

    def show_note_by_id(self):
        choice_id = input("Введите id искомой записки: ")
        for note in self.notes:
            if note.id == choice_id:
                print(f"Искомая записка:\n{note}\n")

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

    def save_data(self):
        save_choice = input(
            "Сохранить данные в файл csv?\n1 - да\n2 - нет\nВведите 1 или 2: ")
        if save_choice == "1":
            arr = []
            for note in self.notes:
                arr.append([note.id, note.date, note.title, note.content])
            with open("notes.csv", "w+", encoding="utf-8") as csv_wr:
                writter = csv.writer(csv_wr, lineterminator="\r")
                for i in range(len(arr)):
                    writter.writerow(arr[i])
            csv_wr.close()
            print("Данные успешно сохранены в файл!\n")
        elif save_choice == "2":
            print("Сохранение отменено!\n")
            return
        else:
            print("Такого пункта нет!\n")

    def load_data(self):
        file = open("notes.csv", encoding="utf-8")
        data_list = []
        for line in file:
            split_line = line.rstrip(line[-1]).split(",")
            data_list.append((split_line))
        file.close()
        print("Список заметок из файла:")
        for i in range(len(data_list)):
            print()
            for j in range(4):
                print(f"Заметка №{data_list[i][j]}")
        print()

    def sort_by_date(self):
        for i in range(len(self.notes) - 1):
            if (self.notes[i].date < self.notes[i + 1].date):
                buf = self.notes[i].date
                self.notes[i].date = self.notes[i + 1].date
                self.notes[i + 1].date = buf
        return self.notes