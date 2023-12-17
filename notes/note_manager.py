from collections import UserDict


class NotesRecord:
    """Class NotesRecord recording notes to Notes.

            Attributes:
                self.notes: Notes.
                
            Methods:
                add_notes: adding of notes to Notes
                delete_notes: deleating of notes
            """
    def __init__(self, notes):
        self.notes = notes
        self.notes = []

    def add_notes(self, note, tags=None): # tags=None if we need it(if not, delit it)
        self.tasks.append({'note_name': note,'tags': tags})
        print(f'Enjoy, you had added "{note}" to your notes.')

    def delete_notes(self, note_to_delete):
        if not note_to_delete:
            print("Please enter note you would like to delete")
        else:
            for element in self.notes:
                if note_to_delete in element['note_name']:
                    element['note_name'].remove(note_to_delete)
                    return element


class Notes(UserDict):
    def add_note_record(self, note_record: NotesRecord):
        self.data[note_record.notes] = note_record   
        return self.data
