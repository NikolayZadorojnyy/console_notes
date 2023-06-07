from datetime import datetime
class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.date = datetime.now().strftime('%Y %B %d %A | %H:%M')

    def __str__(self) -> str:
        return f"Заметка №{self.id}\nДата: {self.date}\nЗаголовок: {self.title}\nСодержимое: {self.content}"
