class Note:

    def __init__(self, id, title, content, date):
        self.id = id
        self.title = title
        self.content = content
        self.date = date

    def __str__(self) -> str:
        return f"Заметка №{self.id} дата: {self.date}\n{self.title}\n{self.content}"
