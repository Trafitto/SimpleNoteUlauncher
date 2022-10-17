from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from note import SimpleNoteManager
import logging

DEFAULT_ICON = 'images/icon.png'


class SimpleNoteExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        # File path preference currently not supported
        # extension.preferences['filepath']
        note_manager = SimpleNoteManager()
        query = event.get_argument()
        items = []
        logging.debug(event)
        logging.debug(query)
        if not query:
            notes = note_manager.read_notes()
            for note in notes:
                items.append(ExtensionResultItem(icon=DEFAULT_ICON,
                                                 name=note.note,
                                                 description=note.format_date(),
                                                 on_enter=ExtensionCustomAction({'to_remove': note})))  # add here the the delete
        else:
            items.append(ExtensionResultItem(icon=DEFAULT_ICON,
                                             name=f'Add {query}',
                                             description='Create new note',
                                             on_enter=ExtensionCustomAction({'note': query})))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        # File path preference currently not supported
        # extension.preferences['filepath']
        note_manager = SimpleNoteManager()
        data = event.get_data()
        if data and data.get('note'):
            note_manager.add_note(data['note'])
            note_manager.save_notes()
            items.append(ExtensionResultItem(icon=DEFAULT_ICON,
                                             name='',
                                             description='',
                                             on_enter=HideWindowAction()))
        elif data and data.get('to_remove'):
            note_manager.remove_note(data['to_remove'])
            note_manager.save_notes()
        return RenderResultListAction(items)

if __name__ == '__main__':
    SimpleNoteExtension().run()
