import uuid
import datetime
class SimpleNote(object):
    def __init__(self, uuid: str, timestamp: int, note: str):
        self.uuid = uuid
        self.timestamp = timestamp
        self.note = note.replace('\n', '')

    def __str__(self):
        return f'{self.uuid}|{self.timestamp}|{self.note}'

    def format_date(self):
        return datetime.datetime.fromtimestamp(self.timestamp)

class SimpleNoteManager():
    filepath = ""
    notes: list[SimpleNote] = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(
                SimpleNoteManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.notes = self.read_notes()

    def _format_notes(self):
        return [f'\n' for n in self.notes]

    def read_notes(self):
        if not self.notes or len(self.notes) == 0:
            with open('./simple-note.txt', 'r') as file_:
                for row in file_.readlines():
                    line = row.split('|', 3)
                    if line and len(line) == 3:
                        self.notes.append(SimpleNote(*line))
        return self.notes

    def save_notes(self):
        if self.notes and len(self.notes) > 0:
            with open('./simple-note.txt', 'w') as file_:
                for note in self.notes:
                    print(str(note))
                    if note:
                        file_.write(str(note)+'\n')

    def add_note(self, text:str):
        self.notes.append(SimpleNote(uuid.uuid4(), datetime.datetime.now().timestamp(), text))
    


''' SimpleNoteManager().add_note('test')
SimpleNoteManager().add_note('test2')
SimpleNoteManager().add_note('test3')
SimpleNoteManager().save_notes()
[print(n.note) for n in SimpleNoteManager().read_notes()] '''