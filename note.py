import uuid
class SimpleNote():
    def __init__(self, uuid: str, timestamp: int, note: str):
        self.uuid = uuid
        self.timestamp = timestamp
        self.note = note


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

    def read_notes(self):
        if not self.notes or len(self.notes) == 0:
            with open('simple-note.txt', 'ra') as file:
                row = file.readline().split('|', 3)
                self.notes.append(SimpleNote(*row))
        return self.notes

    def add_note(self, note:SimpleNote):
        self.note.append(note)