from collections import UserDict
from contacts.classes.Name import Name
import json


class NotesRecord:
    """Class NotesRecord recording notes to Notes.

            Attributes:
                self.notes: Notes.

            Methods:
                add_notes: adding of notes to Notes
                delete_notes: deleating of notes
            """
    def __init__(self, title, *notes):
        self.title = title
        if notes is None:
            self.notes=[]
        self.notes = [notes]

    def add_notes(self, note):
        self.notes.append(note)
        print(f'Enjoy, you had added "{note}" to your notes.')

# completely change the title
    def change_title(self, new_title):
        self.title = new_title

# partially modify title
    def edit_title(self, wrong_part, new_part):
        part_of_title = self.title.find(wrong_part)
        if part_of_title == -1:
            print(f'Title has no letters {wrong_part}. Please try again.')
        else:
            new_title = self.title.replace(wrong_part, new_part)
            self.title = new_title

# modify note
    def edit_note(self, wrong_part, new_part):
        check_flag = False
        for note in self.notes:
                if wrong_part in note:
                    new_note = note.replace(wrong_part, new_part)
                    self.notes[self.notes.index(note)] = new_note
                    check_flag = True
        if not check_flag:
                print(f'Notes have no letters {wrong_part}. Please try again.')

    def delete_notes(self, note_to_delete):
        if not note_to_delete:
            print("Please enter note you would like to delete")
        else:
            if note_to_delete in self.notes:
                self.notes.remove(note_to_delete)
                print(f'Note "{note_to_delete}" was successfully deleted.')
            else:
                print(f'Note "{note_to_delete}" that you search is not found.')


class Notes(UserDict):
    def add_note_record(self, record: NotesRecord):
        self.data[record.title] = record
        return self.data

    def search_in_note_by_title(self, title):
        titles = self.data.values
        print("note in search by titles: ", titles)

    def search_notes_record(self):
        search_info = input("Enter the search parameter: ").lower()
        
        for note in self.data.values():
            print(note)
            print(type(note))
            search_by_title = note.title.lower().find(search_info)
            search_by_notes = str([n for n in note.notes]).find(search_info)
            if search_by_title > -1 or search_by_notes > -1:
                return note.title


    def delete_note(self):
        delete_info = input("Enter the search parameter: ").lower()
        result_list = []
        for note in self.data.values():
            search_by_title = note.title.lower().find(delete_info)
            search_by_notes = str([n.lower() for n in note.notes]).find(delete_info)
            if search_by_title > -1 or search_by_notes > -1:
                result_list.append(note)
        dict_with_number = dict(zip([i+1 for i in range(len(result_list))], [i.title for i in result_list]))
        print(dict_with_number)
        print('Please choose note number to delete?')
        delete_i = int(input())
        for key, value in dict_with_number.items():
            if key == delete_i:
                del self.data[value]

    @staticmethod
    def convert_to_serializable(notesbook):
        """Converts the NotesBook object to a serializable format.

        Args:
            notesbook (NotesBook): The NotesBook object to convert.

        Returns:
            dict: A dictionary containing the serialized data.
        """
        serializable_data = {}
        for key, record in notesbook.items():
            serializable_data[str(key)] = {
                "title": record.title.value,
                "notes": record.notes
            }
        return serializable_data

    def save_to_file_notes(self, filename):
        data_to_serialize = Notes.convert_to_serializable(self)
        try:
            with open(filename, "w", encoding="utf-8") as json_file:
                json.dump(data_to_serialize, json_file, indent=4)
                json_file.write('\n')
            print(f'Notes saved to {filename} successfully.')
        except Exception as e:
            print(f'Error saving notes to {filename}: {e}')


    @ staticmethod
    def load_from_file(filename):
        try:
            with open(filename, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            notesbook = Notes()
            for key, value in data.items():
                title = key
                notes = value["notes"]
                record =  NotesRecord(title, notes)
                notesbook.add_note_record(record)
            # print(f'Notes loaded from {filename} successfully.')
            return notesbook
        except Exception as e:
            print(f'Error loading notes from {filename}: {e}')
            return Notes()  # Return a new instance in case of an error