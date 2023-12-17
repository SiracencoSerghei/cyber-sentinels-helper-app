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


    def save_notes(self):
        with open(self.file, "w", newline="", encoding="utf-8") as json_file:
            json.dump(self.notes, json_file)

class Notes(UserDict):
    def add_note_record(self, note_record: NotesRecord):
        self.data[note_record.title] = note_record   
        return self.data
    
    def search_note(self):
        search_info = input().lower()
        for note in self.data.values():
            search_by_title = note.title.lower().find(search_info)
            search_by_notes = str([n.lower() for n in note.notes]).find(search_info)
            if search_by_title > -1 or search_by_notes > -1:
                print(note.title) 

    #we can change return info

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
    


if __name__ == "__main__":
    pass