from model import *

# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.

note_1 = Note("1", "ААА", "Первая заметка")
note_2 = Note("2", "BBB", "Вторая заметка")
note_3 = Note("3", "CCC", "Третья заметка")
notes: Note = [note_1, note_2, note_3]
# print(type(notes))
# arr = []
# for note in notes:
#     arr.append(note.id)
#     arr.append(note.id)
#     arr.append(note.id)
#     arr.append(note.id)
# print(arr)

model_obj = Model(notes)
# model_obj.create_note()
# model_obj.show_note_by_id()
# model_obj.edit_note()
model_obj.save_data()
# print(model_obj.load_data("notes.csv"))