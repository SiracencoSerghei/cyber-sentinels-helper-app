from collections import UserDict
import json


class NotesRecord:
    """Class NotesRecord recording notes to Notes.

            Attributes:
                self.notes: Notes.
                
            Methods:
                add_notes: adding of notes to Notes
                delete_notes: deleating of notes
            """
    def __init__(self, title, filename):
        self.title = title
        self.file = filename
        self.notes = []

    def add_notes(self, note): 
        self.notes.append(note)
        print(f'Enjoy, you had added "{note}" to your notes.')

    def delete_notes(self, note_to_delete):
        if not note_to_delete:
            print("Please enter note you would like to delete")
        else:
            if note_to_delete in self.notes:
                self.notes.remove(note_to_delete)
                print(f'Note "{note_to_delete}" was successfully deleted.')
            else:
                print(f'Note "{note_to_delete}" that you search is not found.')


    def save_notes(self):
        with open(self.file, "w", newline="", encoding="utf-8") as json_file:
            json.dump(self.notes, json_file)

class Notes(UserDict):
    def add_note_record(self, note_record: NotesRecord):
        self.data[note_record.title] = note_record   
        return self.data
    


if __name__ == "__main__":
    pass