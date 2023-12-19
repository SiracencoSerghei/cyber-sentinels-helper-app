from notes.note_manager import NotesRecord
from notes.note_manager import Notes
from contacts.classes.Name import Name
from decorators.input_errors import input_errors

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


# @input_errors
def load_notes_from_file():
    try:
        return Notes.load_from_file('outputs/notes.json')
    except (FileNotFoundError, EOFError) as e:
        print(f"{RED}Error loading address book: {e}{RESET}")
        print(f"{YELLOW}Creating a new address book.{RESET}")
        return Notes()  # Creating a new instance

@input_errors
def add_note_record_to_notes(notesbook, title, *notes):
    """Add a note to the notes book.

    Args:
        book (NotesBook): The NotesBook instance.
        title (str): The title of the note.
        *notes (str): One or more notes to associate with the note.

    Returns:
        str: A message indicating the result of the operation.
    """
    notes_list = []
    notes =notes[0]
    notes1 = ' '.join(notes)
    notes_list.append(notes1)

    record = notesbook.add_note_record(title)
    print(record)
    if record is None:
        record = NotesRecord(title, notes1)
        notesbook.add_note_record(record)

    notesbook.save_to_file_notes('outputs/notes.json')
    return f"{GREEN}Note {title} was added successfully!{RESET}"


def add_note_to_book(book):
    title = input("Enter the title for the note: ")
    note = input("Enter a note to add: ")
    note_record = NotesRecord(title)
    note_record.add_notes(note)
    book.add_note_record(note_record)
    print(f'Note "{title}" has been added successfully.')


def edit_note_in_book(book):
    title = input("Enter the title of the note to edit: ")
    if title in book.data:
        note_record = book.data[title]
        new_title = input(f"Enter a new title for the note (press Enter to keep '{title}'): ")
        new_notes = input(f"Enter new notes for the note (press Enter to keep the existing notes): ")
        note_record.edit_notes(new_title or title, new_notes)
        print(f'Note "{title}" has been edited successfully.')
    else:
        print(f'Note "{title}" not found in the book.')


def delete_note_from_book(book):
    title = input("Enter the title of the note to delete: ")
    book.delete_note_record(title)

