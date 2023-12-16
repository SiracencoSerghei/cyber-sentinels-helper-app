from datetime import datetime

from contacts.classes.Name import Name
from contacts.classes.Phone import Phone
from contacts.classes.Birthday import Birthday
from contacts.classes.Email import Email
from contacts.classes.Status import Status
from contacts.classes.Note import Note


class Record:
    """Клас Record представляє запис контакту в телефонній книзі.

            Attributes:
                self.name (Name): Ім'я контакту.
                self.phones (list of Phone): Список телефонних номерів контакту.
                self.birthday (Birthday): Дата народження контакту.

            Methods:
                days_to_birthday(): Повертає кількість днів до наступного дня народження контакту,
                якщо вказана дата народження.
                add_birthday(value): Додає дату народження контакту.
                edit_birthday(new_value): Змінює дату народження контакту.
                add_phone(phone): Додає телефонний номер контакту.
                remove_phone(phone): Видаляє телефонний номер контакту.
                edit_phone(old_phone, new_phone): Редагує існуючий телефонний номер контакту.
                find_phone(phone): Знаходить телефонний номер контакту за значенням номера.
                get_all_phones(): Повертає список всіх телефонних номерів контакту.
            """

    def __init__(self, name, birthday=None, email=None, status=None, note=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = []
        self.email = Email(email) if email else None
        self.status = Status(status) if status else None
        self.note = Note(note) if note else None

    def days_to_birthday(self):
        """Повертає кількість днів до наступного дня народження контакту, якщо вказана дата народження.

                Returns:
                    int or None: Кількість днів до наступного дня народження, або None, якщо дата народження не вказана.
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

    def edit_attribute(self, field_name, new_value):
        """Edit a field or attribute in the contact record.

        Args:
            field_name (str): The name of the field or attribute to edit.
            new_value: The new value to set for the field or attribute.

        Raises:
            ValueError: If the field name is invalid or not supported.
        """
        match field_name:
            case "name":
                self.name = Name(new_value)
            case "birthday":
                self.birthday = Birthday(new_value) if new_value else None
            case "email":
                self.email = Email(new_value)
            case "status":
                self.status = Status(new_value)
            case "note":
                self.note = Note(new_value)
            case "phone":
                # Assume new_value is a phone number
                if not isinstance(new_value, Phone):
                    new_value = Phone(new_value)

                # Check if the phone number already exists, and update if it does
                for i, phone in enumerate(self.phones):
                    if phone.value == new_value.value:
                        self.phones[i] = new_value
                        break
                else:
                    # If the phone number doesn't exist, add it
                    self.phones.append(new_value)
            case _:
                raise ValueError(f"Invalid or unsupported field name: {field_name}")

    def add_phone(self, phone):
        """Додає телефонний номер контакту.

        Args:
            phone (str): Телефонний номер для додавання.
        """
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        """Видаляє телефонний номер контакту.

        Args:
            phone (str): Телефонний номер для видалення.
        """
        if phone in [p.value for p in self.phones]:
            self.phones = [p for p in self.phones if p.value != phone]



    def find_phone(self, phone):
        """Знаходить телефонний номер контакту за значенням номера.

        Args:
            phone (str): Телефонний номер для пошуку.

        Returns:
            Phone or None: Знайдений телефоний номер або None, якщо не знайдено.
        """
        for p in self.phones:
            if p.value == phone:
                return p

    def get_all_phones(self):
        """Повертає список всіх телефонних номерів контакту.

        Returns:
            list of str: Список телефонних номерів контакту.
        """
        result = [p.value for p in self.phones]
        return result

    def __str__(self):
        return f"Contact name: {self.name.value},birthday: {self.birthday}, " \
               f"phones: {'; '.join(p.value for p in self.phones)}" \
               f"email: {self.email}, status: {self.status}" \
               f"note: {self.note}"\

