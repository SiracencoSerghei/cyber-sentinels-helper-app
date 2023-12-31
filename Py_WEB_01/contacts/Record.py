import unittest
from datetime import datetime

from contacts.Name import Name
from contacts.Phone import Phone
from contacts.Birthday import Birthday
from contacts.Email import Email
from contacts.Address import Address
from contacts.Status import Status
from contacts.Note import Note
from decorators.input_errors import input_errors



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

    def __init__(self, name, birthday=None, email=None, address = None, status=None, note=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = []
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.status = Status(status) if status else None
        self.note = Note(note) if note else None


    @input_errors
    def edit_name(self, new_value):
        self.name.__set__(self, new_value)


    def days_to_birthday(self):
        return self.birthday.days_to_birthday(self.birthday)


    def add_phone(self, phone):
        """Додає телефонний номер контакту.

        Args:
            record (Record): Об'єкт класу Record.
            phone (str): Телефонний номер для додавання.
        """
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        self.phones.append(phone)

    @input_errors
    def remove_phone(self, phone):
        """Видаляє телефонний номер контакту.

        Args:
            record (Record): Об'єкт класу Record.
            phone (str): Телефонний номер для видалення.
        """
        if phone in [p.value for p in self.phones]:
            self.phones = [p for p in self.phones if p.value != phone]

    @input_errors
    def edit_phone(self, old_phone, new_phone):
        """Редагує існуючий телефонний номер контакту.

        Args:
            record (Record): Об'єкт класу Record.
            old_phone (str): Старий телефонний номер для редагування.
            new_phone (str): Новий телефонний номер.

        Raises:
            ValueError: Якщо старий телефонний номер не знайдено.
        """
        is_found_old_phone = False
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                is_found_old_phone = True
        if not is_found_old_phone:
            raise ValueError('Phone not found')

    @input_errors
    def find_phone(self, phone):
        """Знаходить телефонний номер контакту за значенням номера.

        Args:
            record (Record): Об'єкт класу Record.
            phone (str): Телефонний номер для пошуку.

        Returns:
            Phone or None: Знайдений телефоний номер або None, якщо не знайдено.
        """
        for p in self.phones:
            if p.value == phone:
                return p

    @input_errors
    def get_all_phones(self):
        """Повертає список всіх телефонних номерів контакту.

        Args:
            record (Record): Об'єкт класу Record.

        Returns:
            list of str: Список телефонних номерів контакту.
        """
        result = [p.value for p in self.phones]
        return result



    def __str__(self):
        return (
            f"Contact name: {self.name.value},\n"
            f"birthday: {self.birthday},\n"
            f"phones: {'; '.join(p.value for p in self.phones)},\n"
            f"email: {self.email},\n"
            f"address: {self.address},\n"
            f"status: {self.status},\n"
            f"note: {self.note}"
        )



if __name__ == '__main__':
    record = Record("Jone Doe", "2023-12-23", "AZE@AZE.AZE", "Denderleeuw", "work", "to call")
    print(record)
    print("+++++++++++++++++")
    record.edit_name("Joanne")
    print(record)

    record.add_phone("1234567890")
    print(record.get_all_phones())
    
    record.edit_phone("1234567890", "0987654321")
    print(record.get_all_phones())
    
    