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
    def add_note_record(self, note_record: NotesRecord):
        self.data[note_record.title] = note_record
        return self.data

    def search_in_note_by_title(self, title):
        titles = self.data.values
        print(titles)

    def search_note(self,):
        search_info = input().lower()
        for note in self.data.values():
            search_by_title = note.title.lower().find(search_info)
            search_by_notes = str([n.lower() for n in note.notes]).find(search_info)
            if search_by_title > -1 or search_by_notes > -1:
                return note.title


    def delete_note(self):
        delete_info = input().lower()
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

    def save_to_file_notes(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as json_file:
                data = {title: record.notes for title, record in self.data.items()}
                json.dump(data, json_file, separators=(',', ':'))
                json_file.write('\n')
            print(f'Notes saved to {filename} successfully.')
        except Exception as e:
            print(f'Error saving notes to {filename}: {e}')


    @ staticmethod
    def load_from_file(filename):
        try:
            with open(filename, "r", encoding="utf-8") as json_file:
                notes_book = Notes()
                for line in json_file:
                    data = json.loads(line.strip())
                    title = data["title"]
                    notes = data["notes"]
                    note_record = NotesRecord(title)
                    note_record.notes = notes
                    notes_book.data[title] = note_record
            print(f'Notes loaded from {filename} successfully.')
            return notes_book
        except Exception as e:
            print(f'Error loading notes from {filename}: {e}')
            return Notes()  # Return a new instance in case of an error


#save to file by line
# class SaveToNotes(Notes):
#     def save_notes(self):
#         filename = "Notes.json"
#         try:
#             with open(filename, "a", encoding="utf-8") as json_file:
#                 data = {title: record.notes for title, record in self.data.items()}
#                 json.dump(data, json_file, separators=(',', ':'))
#                 json_file.write('\n')
#             print(f'Notes saved to {filename} successfully.')
#         except Exception as e:
#             print(f'Error saving notes to {filename}: {e}')

if __name__ == "__main__":
    note_record_1 = NotesRecord(title="Cake")

    # Add some notes
    note_record_1.add_notes("flour")
    note_record_1.add_notes("sugar")
    note_record_1.add_notes("eggs")

    note_record_1.change_title("By_list")

    note_record_1.edit_note("flour", "milk")

    note_record_1.delete_notes("eggs")

    # Create a new NotesRecord with a modified title
    modified_note_record = note_record_1.edit_title("By", "By Ingredients")

    # Save notes to a file
    # save_notes_instance_1 = SaveToNotes()
    # save_notes_instance_1.add_note_record(note_record_1)
    # save_notes_instance_1.save_notes()


    note_record_1 = NotesRecord(title="Coffe")

    # Add some notes
    note_record_1.add_notes("Cafe Late")
    note_record_1.add_notes("Irish Coffe")


    note_record_1.change_title("Coffe-choose")

    note_record_1.edit_note("Cafe Late", "Capuchino")

    #note_record_1.delete_notes("eggs")

    # Create a new NotesRecord with a modified title
    modified_note_record = note_record_1.edit_title("By", "By Ingredients")

    # # Save notes to a file
    # save_notes_instance_1 = SaveToNotes()
    # save_notes_instance_1.add_note_record(note_record_1)
    # save_notes_instance_1.save_notes()


if __name__ == "__main__":
    pass


#
# from collections import UserDict
# import json
# from contacts.classes.Name import Name
#
#
# class NoteRecord:
#     """Class NoteRecord recording notes to Notes.
#
#     Attributes:
#         self.notes: Notes.
#
#     Methods:
#         add_notes: adding of notes to Notes
#         edit_notes: editing title and notes
#         delete_notes: deleting of notes
#     """
#
#     def __init__(self, title):
#         self.title = Name(title)
#         self.notes = []
#
#     def add_notes(self, *notes):
#         self.notes.extend(notes)
#         print(f'Enjoy, you had added {", ".join(map(str, notes))} to your notes.')
#
#     def edit_notes(self, new_title=None, new_notes=None):
#         if new_title is not None:
#             self.title = new_title
#         if new_notes is not None:
#             self.notes = new_notes
#         print(f'Note "{self.title}" has been edited successfully.')
#
#     def delete_notes(self):
#         self.title = None
#         self.notes = []
#         print(f'Note has been deleted successfully.')
#
# class NotesBook(UserDict):
#     def add_note_record(self, note_record: NoteRecord, *notes):
#         note_record.add_notes(*notes)
#         self.data[note_record.title] = note_record
#         return self.data
#
#
#     def search_note(self, title):
#         title = title.lower()
#         for record in self.data.values():
#             if record.title.lower() == title:
#                 return record
#         return None
#
#
#
#     def delete_note_record(self, title):
#         if title in self.data:
#             del self.data[title]
#             print(f'Note record "{title}" has been deleted successfully.')
#         else:
#             print(f'Note record "{title}" not found.')
#
#     @staticmethod
#     def convert_to_serializable(notesbook):
#         """Converts the NotesBook object to a serializable format.
#
#         Args:
#             notesbook (NotesBook): The NotesBook object to convert.
#
#         Returns:
#             dict: A dictionary containing the serialized data.
#         """
#         serializable_data = {}
#         for key, record in notesbook.items():
#             serializable_data[str(key)] = {"title": str(record.title),
#                                            "notes": [str(note) for note in record.notes]}
#         return serializable_data
#
#     def save_to_file(self, file_name):
#         """
#         Save the instance to a JSON file.
#
#         Args:
#             file_name (str): The name of the file to save the instance.
#
#         Returns:
#             None
#         """
#         data_to_serialize = NotesBook.convert_to_serializable(self)
#         with open(file_name, 'w', encoding="utf-8") as json_file:
#             json.dump(data_to_serialize, json_file, indent=4)
#
#     @classmethod
#     def load_from_file(cls, filename="notes.json"):
#         try:
#             with open(filename, "r", encoding="utf-8") as json_file:
#                 notes_book = cls()  # create an instance of NotesBook
#                 for line in json_file:
#                     data = json.loads(line.strip())
#                     title = data["title"]
#                     notes = data["notes"]
#                     note_record = NoteRecord(title)
#                     note_record.notes = notes
#                     notes_book.data[title] = note_record
#             print(f'Notes loaded from {filename} successfully.')
#             return notes_book
#         except Exception as e:
#             print(f'Error loading notes from {filename}: {e}')
#             return cls()  # Return a new instance in case of an error