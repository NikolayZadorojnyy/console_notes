from view import *
from presenter import *
from model import *

# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.

# note_1 = Note("1", "ААА", "Первая заметка")
# note_2 = Note("2", "BBB", "Вторая заметка")
# note_3 = Note("3", "CCC", "Третья заметка")
notes: Note = []

model_obj = Model(notes)
view_obj = View()
presenter_obj = Presenter(model_obj, view_obj)
presenter_obj.start()