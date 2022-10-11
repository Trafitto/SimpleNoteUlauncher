from asyncore import file_dispatcher
import uuid
import datetime
import logging
import os


class SimpleNote(object):
    def __init__(self, uuid: str, timestamp: float, note: str):
        self.uuid = uuid
        self.timestamp = float(timestamp)
        self.note = note.replace('\n', '')

    def __str__(self):
        return f'{self.uuid}|{self.timestamp}|{self.note}'

    def format_date(self):
        date = datetime.datetime.fromtimestamp(self.timestamp)
        return date.strftime('%d/%m/%Y')


class SimpleNoteManager():
    notes: list[SimpleNote] = []
    filepath = './simple-note.txt'
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(
                SimpleNoteManager, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        if not os.path.exists(self.filepath):
            file_ = open(self.filepath, 'x') 
            file_.close()
        self.notes = self.read_notes()

    def _format_notes(self):
        return [f'\n' for n in self.notes]

    def read_notes(self):
        if not self.notes or len(self.notes) == 0:
            with open(self.filepath, 'r') as file_:
                for row in file_.readlines():
                    line = row.split('|', 3)
                    if line and len(line) == 3:
                        self.notes.append(SimpleNote(*line))
        return self.notes

    def save_notes(self):
        if self.notes and len(self.notes) > 0:
            with open(self.filepath, 'w') as file_:
                for note in self.notes:
                    print(str(note))
                    if note:
                        file_.write(str(note)+'\n')

    def add_note(self, text: str):
        self.notes.append(SimpleNote(
            uuid.uuid4(), datetime.datetime.now().timestamp(), text))


''' SimpleNoteManager().add_note('test')
SimpleNoteManager().add_note('test2')
SimpleNoteManager().add_note('test3')
SimpleNoteManager().save_notes()
[print(n.note) for n in SimpleNoteManager().read_notes()] '''
