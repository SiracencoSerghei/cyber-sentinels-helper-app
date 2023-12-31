
from decorators.input_errors import input_errors
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from contacts.AddressBook import AddressBook

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


#  ================================

class ContactBot:
    # noinspection PyTypeChecker
    def __init__(self):
        self.__known_commands = ("Add Contact", "Edit Contact", "Find In Contacts", "Delete Contact",
                                 "Show Contact", "Days To Birthday", "Exit")
        self.session = PromptSession(
            history=FileHistory('outputs/history.txt'),
            completer=WordCompleter(self.__known_commands),
        )


    def run(self):
        """Main function for user interaction.

               Returns:
                   None
               """
        try:
            book = AddressBook.load_json_from_file('outputs/address_book.json')
        except (FileNotFoundError, EOFError) as e:
            print(f"{RED}Error loading address book: {e}{RESET}")
            print(f"{YELLOW}Creating a new address book.{RESET}")
            book = AddressBook()  # Creating a new instance
        while True:
            user_input = self.session.prompt("... ")
            if user_input == "":
                print(f"{RED}Empty input !!!{RESET}")
                continue
            input_data = user_input.split()
            input_command = input_data[0].lower()
            if input_command in self.__exit_commands:
                print(f"{RED}{good_bye()}{RESET}")
                break
            elif input_command in self.__known_commands:
                match input_command:
                    case 'exit':
                        print(f"{RED}{good_bye()}{RESET}")
                        break
                    case "find_all_in_contacts":
                        try:
                            search_param = input_data[1]
                            result = book.find(search_param)
                            print(f"{GREEN}Matching records:\n{result}{RESET}")
                        except IndexError:
                            print(f"{RED}You have to provide a search parameter after 'find'.{RESET}")

                    case "file-manager":
                        try:
                            start_path = os.path.expanduser("~")
                            display_directory_contents(start_path)
                            print(f"{GREEN}Folder was sorted{RESET}")
                        except Exception as e:
                            # print(f"{RED}Error: '{e}'{RESET}")
                            pass
                    case "show-contact":
                        try:
                            self.book = AddressBook.load_from_file('outputs/address_book.json')
                            self.showall(int(input_data[1]) if len(input_data) > 1 else None)
                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case "show-notes":
                        try:
                            self.notesbook = Notes.load_from_file('outputs/notes.json')
                            show_notes(self.notesbook, int(input_data[1]) if len(input_data) > 1 else None)
                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case "show-todos":
                        try:
                            self.todobook = ToDoBook.load_from_file('outputs/todo.json')
                            show_todo(self.todobook, int(input_data[1]) if len(input_data) > 1 else None)
                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case 'add-contact':
                        try:
                            print(add_contact(self.book, input_data[1], input_data[2:]))
                        except IndexError:
                            print(f"{RED}You have to put name(or name-surname) and phone(s) after add-contact. "
                                  f"Example: \n"
                                  f"add-contact <name> <phone1> <phone2> ...{RESET}")
                    case 'add-note':
                        if len(input_data) >= 2:
                            print(add_note_record_to_notes(self.notesbook, input_data[1], input_data[2:]))
                        else:
                            print("Invalid input. Usage: add-note <title> <note1> <note2> ...")

                    case 'add-todo':
                        if len(input_data) >= 6:
                            print(add_todo_record_to_file(self.todobook, input_data[1], input_data[2], input_data[3],
                                                          input_data[4], input_data[5:]))
                        else:
                            print("Invalid input. Usage: add-todo <title> <begin date> <end date> <status> <tags> ...")

                    case 'add-tag':
                        self.todobook.add_tag()

                    case 'edit-contact':
                        edit_contact(self.book)

                    case 'edit-note':
                        edit_notes(self.notesbook)

                    case 'edit-todo':
                        edit_todo_list(self.todobook)

                    case 'delete-contact':
                        self.book.delete_contact()

                    case 'delete-note':
                        self.notesbook.delete_note()

                    case 'delete-todo':
                        self.todobook.delete_task()

                    case 'delete-tag-in-todo':
                        self.todobook.delete_tag_in_todo()

                    case "days-to-birthday":
                        if len(input_data) < 2:
                            print(
                                f"{RED}You need to provide a name after 'days-to-birthday'. "
                                f"Example: days-to-birthday <name>{RESET}"
                            )
                        else:
                            print(self.days_to_birthday(input_data[1]))


            else:
                print(f"{RED}Don't know this command{RESET}")


if __name__ == '__main__':
    bot = ContactBot()
    bot.run()
