

def edit_contact(book):
    search_param = input("Enter the search parameter: ")
    book.edit_contact(search_param)

def edit_notes(notesbook: object):
    result = notesbook.search_notes_record()
    print(result)
    print(type(result))



