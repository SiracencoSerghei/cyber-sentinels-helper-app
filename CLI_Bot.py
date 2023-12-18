from pathlib import Path
from contacts.classes.AddressBook import AddressBook
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from decorators.input_errors import input_errors
from utils.sanitize_phone_nr import sanitize_phone_number
from rich.console import Console
from rich.table import Table
from file_manager.sort_dir import sort_folder
from utils.help import help
from utils.address_book_functions import add_contact, greeting, good_bye, load_address_book

# I'm applying the decorator directly, overwriting the function
sanitize_phone_number = input_errors(sanitize_phone_number)

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


#  ================================

class Bot:
    def __init__(self):
        self.__known_commands = (
            "help", "add", "edit", "find", "delete",
            "show", "hello", "days-to-birthday", "sort")
        self.__exit_commands = ("goodbye", "close", "exit", ".")
        self.book = load_address_book()
        self.session = PromptSession(
            history=FileHistory('history.txt'),
            completer=WordCompleter(self.__known_commands + self.__exit_commands),
        )

    @input_errors
    def showall(self, chunk_size=1):
        """Display all contacts in the address book.

        Returns:
            None
        """
        console = Console()

        table = Table(title="Address Book")
        table.add_column("Name", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Phones", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Birthday", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Email", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Address", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Status", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Note", style="blue", justify="center", min_width=10, max_width=30)

        records = list(self.book.values())
        num_records = len(records)
        i = 0
        while i < num_records:
            chunk = records[i:i + chunk_size]
            for record in chunk:
                name = record.name.value
                phones = "; ".join([str(phone) for phone in record.phones])
                birthday = str(record.birthday) if record.birthday else "N/A"
                email = record.email.value if record.email else "N/A"
                address = record.address.value if record.address else "N/A"
                status = record.status.value if record.status else "N/A"
                note = record.note.value if record.note else "N/A"

                table.add_row(name, phones, birthday, email, address, status, note)

            table.add_row("=" * 30, "=" * 30, "=" * 30, "=" * 30, "=" * 30, "=" * 30, "=" * 30)
            i += chunk_size

            if i < num_records:
                # Wait for Enter keypress to continue
                console.print(table)
                input(f"{PINK}Press Enter to show the next chunk...{RESET}")

        console.print(table)

    @input_errors
    def get_phone(self, name):
        """Retrieve the phone numbers associated with a contact.

            Args:
                name (str): The name of the contact.

            Returns:
                str: A message containing the contact's name and phone numbers.
            """
        if name in self.book.data:
            record = self.book.data[name]
            return f"{GREEN}{name} was found with phones - {'; '.join(record.get_all_phones())}{RESET}"
        else:
            return f"{RED}There is no contact with this name!{RESET}"

    @input_errors
    def days_to_birthday(self, name):
        """Calculate the number of days to the next birthday for a contact.

        Args:
            name (str): The name of the contact.

        Returns:
            str: A message indicating the number of days to the next birthday or an error message.
        """
        contact = self.book.find_name(name)

        if contact is None:
            return f"{RED}There is no contact with the name '{name}'{RESET}"

        if contact.birthday:
            days = contact.days_to_birthday()
            if days > 0:
                return f"{GREEN}{name} has {days} days before their next birthday{RESET}"
            elif days == 0:
                return f"{GREEN}{name}'s birthday is today!{RESET}"
            else:
                # will never be executed.... because of Record class....
                return f"{GREEN}{name}'s birthday is in {-days} days{RESET}"
        else:
            return f"{RED}{name} has no birthday set{RESET}"

    def run(self):
        """Main function for user interaction.

               Returns:
                   None
               """
        try:
            book = AddressBook.load_from_file('outputs/address_book.json')

        except (FileNotFoundError, EOFError) as e:
            print(f"{RED}Error loading address book: {e}{RESET}")
            print(f"{YELLOW}Creating a new address book.{RESET}")
            book = AddressBook()  # Creating a new instance
        while True:
            print(f"{YELLOW}If don't now the commands, enter 'help' please{RESET}")
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
                    case 'help':
                        help()
                    case 'hello':
                        print(f"{BLUE}{greeting()} {RESET}")
                    case 'add':
                        try:
                            print(add_contact(self.book, input_data[1], input_data[2]))
                        except IndexError:
                            print(f"{RED}You have to put name and phone after add. Example: \n"
                                  f"add <name> <phone>{RESET}")
                    case 'edit':
                        try:
                            edit_type = input_data[1].lower()
                            if edit_type == 'contact':
                                search_param = input("Enter the search parameter: ")
                                book.edit_contact(search_param)
                            elif edit_type == 'note':
                                # edit_note()
                                pass
                            elif edit_type == 'todolist':
                                # edit_todolist()
                                pass
                            else:
                                print(f"{RED}Invalid edit type. Supported types: contact, note, todolist{RESET}")
                        except IndexError:
                            print(f"{RED}You need to provide an edit type after 'edit'.{RESET}\n"
                                  f"{GREEN}for example: edit contact or note or todo{RESET}")

                    case "delete":
                        # Delete an entry from the address book, notes, or to-do list.
                        try:

                            delete_type = input_data[1].lower()
                            search_param = input(f"Enter the {delete_type} to delete: ")
                            if delete_type == 'contact':
                                result = self.book.find(search_param)
                                delete_method = self.book.del_record
                            elif delete_type == 'note':
                                # Implement your note deletion logic and method here
                                pass
                            elif delete_type == 'todolist':
                                # Implement your to-do list deletion logic and method here
                                pass
                            else:
                                print(f"{RED}Invalid delete type. Supported types: contact, note, todolist{RESET}")
                                return

                            if not result:
                                print(f"{RED}No {delete_type} found with the specified {delete_type}{RESET}")
                            else:
                                # Display the matching records and confirm deletion
                                print(f"{GREEN}Matching {delete_type}s:\n{result}{RESET}")
                                confirmation = input(
                                    f"Are you sure you want to delete this {delete_type}? (yes/no): ").lower()

                                if confirmation == 'yes':
                                    delete_method(search_param)
                                    print(
                                        f"{GREEN}{delete_type.capitalize()} '{search_param}' deleted successfully{RESET}")
                                else:
                                    print(f"Deletion of {delete_type} canceled.")
                        except Exception as e:
                            print(f"{RED}Error deleting {delete_type}: {e}{RESET}")

                    case "show":
                        try:
                            self.book = AddressBook.load_from_file('outputs/address_book.json')
                            self.showall(int(input_data[1]) if len(input_data) > 1 else 1)

                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case "days-to-birthday":
                        if len(input_data) < 2:
                            print(
                                f"{RED}You need to provide a name after 'days-to-birthday'. "
                                f"Example: days-to-birthday <name>{RESET}"
                            )
                        else:
                            print(self.days_to_birthday(input_data[1]))

                    case "find":
                        try:
                            search_param = input_data[1]
                            result = book.find(search_param)
                            print(f"{GREEN}Matching records:\n{result}{RESET}")
                        except IndexError:
                            print(f"{RED}You have to provide a search parameter after 'find'.{RESET}")

                    case "sort":
                        while True:
                            search_param = input("Enter the sort folder (or leave blank to cancel): ")

                            if not search_param:
                                print("Sorting canceled.")
                                break

                            # Расширяем путь пользователя, чтобы обработать ~ и получаем абсолютный путь
                            # abs_path = os.path.abspath(os.path.expanduser(search_param))

                            try:
                                abs_path = Path(search_param).expanduser()
                                print('abs_path: ', abs_path)
                                # sort_folder(str(abs_path))
                                print(f"{GREEN}Folder was sorted{RESET}")
                                break  # Выход из цикла при успешной сортировке
                            except FileNotFoundError:
                                print(f"{RED}Error: No such file or directory: '{abs_path}'{RESET}")
            else:
                print(f"{RED}Don't know this command{RESET}")
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python sort_dir.py <folder_path>")
#     else:
#         INPUT_FOLDER = sys.argv[1]
#         sort_folder(INPUT_FOLDER)
#     print("Script is done")
#
    # if len(sys.argv) != 2:
    #     print("Usage: python sort_dir.py <folder_path>")
    # else:
    #     INPUT_FOLDER = Path(sys.argv[1]).expanduser()
    #     sort_folder(INPUT_FOLDER)
    # print("Script is done")

# python3 sort_dir.py ~/Desktop/мотлох