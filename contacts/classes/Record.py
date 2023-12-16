from datetime import datetime

from contacts.classes.Name import Name
from contacts.classes.Phone import Phone
from contacts.classes.Birthday import Birthday
from contacts.classes.Email import Email
from contacts.classes.Address import Address
from contacts.classes.Status import Status
from contacts.classes.Note import Note


class Record:
    """Class Record is presenting record of contact to phone book.

            Attributes:
                self.name (Name): Contact name.
                self.phones (list of Phone): List of contacts phone numbers.
                self.birthday (Birthday): Date of contacts birthday.

            Methods:
                days_to_birthday(): Returns the number of days until the contact's next birthday, if that given.
                add_birthday(value): Adding contact's date of birthday.
                edit_birthday(new_value): Changing contact's date of birthday.
                add_phone(phone): Adding contact's phone number.
                remove_phone(phone): Deleting  the contact's phone number.
                edit_phone(old_phone, new_phone): Editing an existing contact phone number.
                find_phone(phone): Finds a contact's phone number by number value.
                get_all_phones(): Returns a list of all phone numbers of a contact.
            """

    def __init__(self, name, birthday=None, email=None, address = None, status=None, note=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = []
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.status = Status(status) if status else None
        self.note = Note(note) if note else None

    def days_to_birthday(self):
        """Returns the number of days until the contact's next birthday, if date of births is given

                Returns:
                    int or None: The number of days until the next birthday, or None, if the date of birth is not given.
                """
        if self.birthday:
            today = datetime.now()
            birthday = datetime.strptime(str(self.birthday), '%Y-%m-%d').replace(year=today.year)

            if today > birthday:
                birthday = birthday.replace(year=today.year + 1)

            delta = birthday - today
            return delta.days
        else:
            return None


    def add_field(self, field_name, value):
        """Add a field to the contact record.

        Args:
            field_name (str): The name of the field to add.
            value: The value to set for the field.

        Raises:
            ValueError: If the field name is invalid or not supported.
        """
        match field_name:
            case "name":
                setattr(self, field_name, Name(value))
            case "birthday":
                setattr(self, field_name, Birthday(value))
            case "email":
                setattr(self, field_name, Email(value))
            case "status":
                setattr(self, field_name, Status(value))
            case "note":
                setattr(self, field_name, Note(value))
            case _:
                raise ValueError(f"Invalid or unsupported field name: {field_name}")

    # def edit_attribute(self, field_name, new_value):
    #     """Edit a field or attribute in the contact record.
    #
    #     Args:
    #         field_name (str): The name of the field or attribute to edit.
    #         new_value: The new value to set for the field or attribute.
    #
    #     Raises:
    #         ValueError: If the field name is invalid or not supported.
    #     """
    #     print(field_name)
    #     print(new_value)
    #     if field_name == "name":
    #         setattr(self, "name", new_value)
    #         print(self.name)
    #     elif field_name == "birthday":
    #         setattr(self.birthday, "value", Birthday(new_value) if new_value else None)
    #     elif field_name == "email":
    #         setattr(self.email, "value", Email(new_value))
    #     elif field_name == "status":
    #         setattr(self.status, "value", Status(new_value))
    #     elif field_name == "note":
    #         setattr(self.note, "value", Note(new_value))
    #     elif field_name == "phone":
    #         # Assume new_value is a phone number
    #         if not isinstance(new_value, Phone):
    #             new_value = Phone(new_value)
    #
    #         # Check if the phone number already exists, and update if it does
    #         for i, phone in enumerate(self.phones):
    #             if phone.value == new_value.value:
    #                 self.phones[i] = new_value
    #                 break
    #         else:
    #             # If the phone number doesn't exist, add it
    #             self.phones.append(new_value)
    #     else:
    #         raise ValueError(f"Invalid or unsupported field name: {field_name}")

    def add_phone(self, phone):
        """Adding contact's phone number.

        Args:
            phone (str): The phone number to adding.
        """
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        """Deleting contact's phone number.

        Args:
            phone (str): The phone number to deleting.
        """
        if phone in [p.value for p in self.phones]:
            self.phones = [p for p in self.phones if p.value != phone]



    def find_phone(self, phone):
        """Finds a contact's phone number by number value.

        Args:
            phone (str): The phone number for searching.

        Returns:
            Phone or None: The phone number found, or None if not found.
        """
        for p in self.phones:
            if p.value == phone:
                return p

    def get_all_phones(self):
        """Returns a list of all phone numbers of a contact.

        Returns:
            list of str: A list of all phone numbers of a contact.
        """
        result = [p.value for p in self.phones]
        return result

    def __str__(self):
        return (
            f"Contact name: {self.name.value},\n"
            f"birthday: {self.birthday},\n"
            f"phones: {'; '.join(p.value for p in self.phones)},\n"
            f"email: {self.email},\n"
            f"status: {self.status},\n"
            f"note: {self.note}"
        )
