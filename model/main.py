from presenter import *
from model import *

# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.

notes: Note = []

model_obj = Model(notes)
view_obj = View()
presenter_obj = Presenter(model_obj, view_obj)
presenter_obj.start()
