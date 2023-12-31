import json
import pathlib
from collections import UserDict
from Record import Record
from rich.console import Console
from rich.table import Table

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


class AddressBook(UserDict):
    """A class representing an address book that stores records."""

    def add_record(self, record):
        """Add a record to the address book.

        Args:
            record (Record): The record to add.

        Returns:
            None
        """
        if not isinstance(record, Record):
            record = Record(record)
        self.data[record.name.value] = record

    def del_record(self, name_to_delete):
        """Delete a record from the address book.

        Args:
            name_to_delete (str): The name of the record to delete.

        Returns:
            None
        """
        try:
            if name_to_delete in self.data:
                del self.data[name_to_delete]
                self.save_to_json_file(
                    "outputs/address_book.json"
                )  # Save changes to file
                print(f"{GREEN}Contact '{name_to_delete}' deleted successfully{RESET}")
            else:
                print(f"{RED}No contact found with the name '{name_to_delete}'{RESET}")
        except Exception as e:
            print(f"{RED}Error deleting contact: {e}{RESET}")

    @staticmethod
    def convert_to_json(address_book):
        """Converts the AddressBook object to a serializable format.

        Args:
            address_book (AddressBook): The AddressBook object to convert.

        Returns:
            dict: A dictionary containing the serialized data.
        """
        json_data = {}
        for key, record in address_book.items():
            json_data[key] = {
                "name": record.name.value,
                "phones": record.get_all_phones(),
                "birthday": str(record.birthday) if record.birthday else None,
                "email": record.email.value if record.email else None,
                "address": record.address.value if record.address else None,
                "status": record.status.value if record.status else None,
                "note": record.note.value if record.note else None
            }
        return json_data

    def save_to_json_file(self, file_name):
        """
        Save the instance to a JSON file.

        Args:
            file_name (str): The name of the file to save the instance. The extension will determine the format.

        Returns:
            None
        """
        data_to_json = AddressBook.convert_to_json(self)

        # Determine the file format based on the extension
        file_format = file_name.split(".")[-1].lower()

        if file_format == "json":
            with open(file_name, "w", encoding="utf-8") as json_file:
                json.dump(data_to_json, json_file, indent=4)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

    @staticmethod
    def load_json_from_file(file_name):
        """
        Load an instance from a JSON file.

        Args:
            file_name (str): The name of the file to load the instance from.

        Returns:
            AddressBook: The loaded instance.
        """
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
                address_book = AddressBook()
                for record_data in data.values():
                    new_record = Record(record_data.get("name", ""))
                    phones = record_data.get("phones", [])
                    birthday = record_data.get("birthday", None)
                    email = record_data.get("email", None)
                    address = record_data.get("address", None)
                    status = record_data.get("status", None)
                    note = record_data.get("note", None)
                    for phone in phones:
                        new_record.add_phone(phone)
                    if birthday == "null":
                        new_record.birthday = None
                    if birthday is not None:
                        new_record.birthday = birthday
                    if email == "null":
                        email = None
                    if email is not None:
                        new_record.email = email
                    if status == "null":
                        status = None
                    if status is not None:
                        new_record.status = status
                    if note == "null":
                        note = None
                    if note is not None:
                        new_record.note = note
                    if address == "null":
                        address = None
                    if address is not None:
                        new_record.address = address
                    address_book.add_record(new_record)
                return address_book
        except (FileNotFoundError, EOFError):
            # Handle the case where the file is not found or empty
            return AddressBook()
    # @staticmethod
    # def show_records(book):
    #     """Display all contacts in the address book.
    #
    #     Returns:
    #         None
    #     """
    #     console = Console()
    #     table = Table(title="Address Book")
    #     first_record = next(iter(book.data.values()), None)
    #
    #     record_attributes = list(first_record.__dict__.keys())
    #     print(first_record)
    #     print(record_attributes)
    #     # Add columns dynamically based on the attributes
    #     for attribute in record_attributes:
    #         column_name = attribute.capitalize()  # Convert attribute name to title case
    #         table.add_column(column_name, style="blue", justify="center", min_width=10, max_width=30)
    #
    #     for _, record in book.items():
    #         # Get attribute values dynamically
    #         row_data = []
    #         for attr in record_attributes:
    #             value = getattr(record, attr)
    #
    #             # Check if the value is printable
    #             if hasattr(value, '__iter__') and not isinstance(value, str):
    #                 # If it's an iterable (like a list or tuple), join its elements
    #                 row_data.append("; ".join(map(str, value)))
    #             else:
    #                 # Otherwise, convert the value to a string
    #                 row_data.append(str(value))
    #
    #         table.add_row(*row_data)
    #
    #     console.print(table)

    def find(self, param) -> UserDict:
        """
        Find records that match the given parameter.

        Args:
            param (str): The search parameter.

        Returns:
            str: A string containing the matching records, separated by newline.

        Note:
            If the search parameter is less than 3 characters, it returns an error message.
        """
        if len(param) < 3:
            return "Sorry, the search parameter must be at least 3 characters."

        result = UserDict()

        for i, record in enumerate(self.values()):
            if param.lower() in record.name.value.lower():
                result[record.name.value] = record
            elif param.isdigit():
                matching_phones = [
                    phone for phone in record.get_all_phones() if param in phone
                ]
                if matching_phones:
                    result[record.name.value] = record
            elif record.birthday and param in str(record.birthday):
                result[record.name.value] = record
            elif record.email and param.lower() in record.email.lower():
                result[record.name.value] = record
            elif record.address and param.lower() in record.address.lower():
                result[record.name.value] = record
            elif record.status and param.lower() in record.status.lower():
                result[record.name.value] = record
            elif record.note and param.lower() in record.note.lower():
                result[record.name.value] = record

        if not result:
            return "No records found for the given parameter."

        # result = '\n'.join(result)
        # print(result)
        # self.show_records(result)
        return result

    def edit_contact(self, search_param):
        if len(search_param) < 3:
            print("Sorry, the search parameter must be at least 3 characters.")
            return

        matching_records = []
        for record in self.values():
            if (
                search_param.lower() in record.name.value.lower()
                or search_param in record.get_all_phones()
            ):
                matching_records.append(record)

        if not matching_records:
            print("No records found for the given parameter.")
            return

        print("Matching records:")
        for i, record in enumerate(matching_records, start=1):
            print(f"{i}. {record.name.value}")

        try:
            choice = int(input("Enter the number of the contact to edit: "))
            if 1 <= choice <= len(matching_records):
                selected_record = matching_records[choice - 1]
                field_name = input(
                    "Enter the field to edit (name, birthday, email, status, note, phone, address): "
                )

                # Check if the entered field name is valid
                if field_name == "name":
                    new_value = input("Enter the new name: ")
                    selected_record.edit_name(new_value)
                    print(
                        f"Contact '{selected_record.name.value}' updated successfully."
                    )
                elif field_name == "birthday":
                    new_value = input("Enter the new birthday: ")
                    selected_record.edit_birthday(new_value)
                    print(
                        f"Contact '{selected_record.name.value}' updated successfully."
                    )
                elif field_name == "email":
                    new_value = input("Enter the new email: ")
                    selected_record.edit_email(new_value)
                    print(
                        f"Contact '{selected_record.name.value}' updated successfully."
                    )
                elif field_name == "status":
                    new_value = input("Enter the new status: ")
                    selected_record.edit_status(new_value)
                    print(
                        f"Contact '{selected_record.name.value}' updated successfully."
                    )
                elif field_name == "note":
                    new_value = input("Enter the new note: ")
                    selected_record.edit_note(new_value)
                    print(
                        f"Contact '{selected_record.name.value}' updated successfully."
                    )
                elif field_name == "phone":
                    old_phone = input("Enter the old phone: ")
                    new_phone = input("Enter the new phone: ")
                    selected_record.edit_phone(old_phone, new_phone)
                    print(
                        f"Contact '{selected_record.name.value}' updated successfully."
                    )
                elif field_name == "address":
                    new_value = input("Enter the new address: ")
                    selected_record.edit_address(new_value)
                    print(
                        f"Contact '{selected_record.name.value}' updated successfully."
                    )
                else:
                    print("Invalid field name. Please enter a valid field name.")
                    return  # Add a return statement here to prevent saving in case of an invalid field

                # After editing, save the changes to the file
                self.save_to_json_file("outputs/address_book.json")

            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


if __name__ == "__main__":
    print("Loading address book from file...")
    book = AddressBook.load_json_from_file("../outputs/address_book.json")
    # print(book)
    # for nam, record in book.items():
    #     print(nam)
    #     print("==============")
    #     print(record)
    #     print("+++++++++++++++++++++++++++++++++++")
    # book.show_records(book)
    req = book.find('333')
    book.show_records(req)
    # rec = book.find("ser")
    # book.show_records(rec)
