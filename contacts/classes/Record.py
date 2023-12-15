from datetime import datetime

from Name import Name
from Phone import Phone
from Birthday import Birthday


class Record:          
    def __init__(self, name, *birthday):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = []

    def add_phone(self, phone):
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        self.phones.append(phone)
            
    def edit_phone(self, old_phone, new_phone):
        is_found_old_phone = False
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                is_found_old_phone = True
        if not is_found_old_phone:
            raise ValueError('Phone not found')
        
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
        return self.phones
        
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        
    def days_to_birthday(self):
        if self.birthday:
            birthdate = datetime(self.birthday.year, self.birthday.month, self.birthday.day)
            date_now = datetime(date_now.year, date_now.month, date_now.day)

            # Виконуємо перевірку чи був ДН у цьому році чи ще ні
            if date_now.date() > birthdate.date():
                next_birthday = birthdate.replace(year=date_now.year + 1)
            else:
                next_birthday = birthdate.replace(year=date_now.year)
            days_till_birthday = (next_birthday - date_now).days
            return days_till_birthday
        else:
            return None
        
    def add_birthday(self, value):
        self.birthday = Birthday(value)

           
    def __str__(self):
        if self.birthday:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday is {self.birthday}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"