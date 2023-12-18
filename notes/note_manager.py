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
    

#save to file by line
class SaveToNotes(Notes):
    def save_notes(self):
        filename = "Notes.json"
        try:
            with open(filename, "a", encoding="utf-8") as json_file:
                data = {title: record.notes for title, record in self.data.items()}
                json.dump(data, json_file,separators=(',', ':'))
                json_file.write('\n')  
            print(f'Notes saved to {filename} successfully.')
        except Exception as e:
            print(f'Error saving notes to {filename}: {e}')

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
    save_notes_instance_1 = SaveToNotes()
    save_notes_instance_1.add_note_record(note_record_1)
    save_notes_instance_1.save_notes()


    note_record_1 = NotesRecord(title="Coffe")
    
    # Add some notes
    note_record_1.add_notes("Cafe Late")
    note_record_1.add_notes("Irish Coffe")
    

    note_record_1.change_title("Coffe-choose")

    note_record_1.edit_note("Cafe Late", "Capuchino")

    #note_record_1.delete_notes("eggs")

    # Create a new NotesRecord with a modified title
    modified_note_record = note_record_1.edit_title("By", "By Ingredients")

    # Save notes to a file
    save_notes_instance_1 = SaveToNotes()
    save_notes_instance_1.add_note_record(note_record_1)
    save_notes_instance_1.save_notes()


if __name__ == "__main__":
    pass