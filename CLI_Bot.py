from contacts.classes.Record import Record
from contacts.classes.AddressBook import AddressBook
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import  FileHistory
from prompt_toolkit.completion import WordCompleter
from decorators.input_errors import input_errors
from utils.sanitize_phone_nr import sanitize_phone_number
from rich.console import Console
from rich.table import Table
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
            "show", "hello", "days-to-birthday")
        self.__exit_commands = ("goodbye", "close", "exit", ".")
        self.book = load_address_book()
        self.session = PromptSession(
            history=FileHistory('history.txt'),
            completer=WordCompleter(self.__known_commands + self.__exit_commands),
        )

    @staticmethod


    @input_errors
    def change_contact(self, name, old_phone, phone):
        """Change the phone number associated with a contact.

            Args:
                name (str): The name of the contact.
                old_phone (str): The old phone number.
                phone (str): The new phone number.

            Returns:
                str: A message indicating the result of the operation.
            """
        if name in self.book.data:
            record = self.book.data[name]
            if old_phone in record.get_all_phones():
                record.edit_phone(old_phone, phone)
                # Save the address book to a file after making the change
                self.book.save_to_file('outputs/address_book.json')
                return (f"{GREEN} Contact {name}: {old_phone} was successfully changed!\n "
                        f"New data: {name}: {phone}{RESET}")
            else:
                return f"{RED}There is no number {phone} in {name} contact{RESET}"
        else:
            return f"{RED}There is no {name} contact!{RESET}"

    @input_errors
    def showall(self, chunk_size=1):
        """Display all contacts in the address book.

        Returns:
            None
        """
        console = Console()

        table = Table(title="Address Book")
        table.add_column("Name", style="blue", justify="center")
        table.add_column("Phones", style="blue", justify="center")
        table.add_column("Birthday", style="blue", justify="center")
        table.add_column("Email", style="blue", justify="center")

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

                table.add_row(name, phones, birthday, email)

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
        print(f"{YELLOW}{contact}{RESET}")

        if contact is None:
            return f"{RED}There is no contact with the name '{name}'{RESET}"

        if contact.birthday:
            days = contact.days_to_birthday()
            print(days)
            if days > 0:
                return f"{GREEN}{name} has {days} days before their next birthday{RESET}"
            elif days == 0:
                return f"{GREEN}{name}'s birthday is today!{RESET}"
            else:
                # will never be executed.... because of Record class....
                return f"{GREEN}{name}'s birthday is in {-days} days{RESET}"
        else:
            return f"{RED}{name} has no birthday set{RESET}"

    @input_errors
    def add_birthday(self, name, date):
        contact = self.book.find_name(name)

        if contact is None:
            return f"{RED}There is no contact with the name '{name}'{RESET}"
        elif contact.birthday:
            return f"{RED}If you want to change {name}'s birthday, use 'edit-birthday <new value>'{RESET}"
        else:
            contact.add_birthday(date)
            # Save the address book to a file after adding the birthday
            self.book.save_to_file('outputs/address_book.json')
            return f"{GREEN} Was update {name}'s birthday date{RESET}"

    @input_errors
    def edit_birthday(self, name, date):
        contact = self.book.find_name(name)

        if contact is None:
            return f"{RED}There is no contact with the name '{name}'{RESET}"
        else:
            contact.edit_birthday(date)
            # Save the address book to a file after editing the birthday
            self.book.save_to_file('outputs/address_book.json')
            return f"{GREEN} Was update {name}'s birthday date{RESET}"


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
                                edit_note()
                            elif edit_type == 'todolist':
                                edit_todolist()
                            else:
                                print(f"{RED}Invalid edit type. Supported types: contact, note, todolist{RESET}")
                        except IndexError:
                            print(f"{RED}You need to provide an edit type after 'edit'.{RESET}\n"
                                  f"{GREEN}for example: edit contact or note or todo{RESET}")

                    case "show":
                        try:
                            self.showall(int(input_data[1]))
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

            else:
                print(f"{RED}Don't know this command{RESET}")
