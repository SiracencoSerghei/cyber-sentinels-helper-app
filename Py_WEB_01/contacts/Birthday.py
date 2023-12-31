from datetime import datetime
from contacts.Field import Field

R = "\033[91m"
RES = "\033[0m"


class Birthday(Field):
    DATE_FORMAT = '%Y-%m-%d'

    @classmethod
    def is_valid_birthday(cls, value):
        try:
            datetime.strptime(value, cls.DATE_FORMAT)
            return True
        except ValueError:
            return False

    def __init__(self, value):
        if not self.is_valid_birthday(value):
            print(f"{R}The birthday date don't added to record{RES}")
            raise ValueError("Not valid birthday date")
        super().__init__(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, new_value):
        if not self.is_valid_birthday(new_value):
            raise ValueError(f"{R}Not valid birthday date{RES}")
        self.value = new_value

    def days_to_birthday(self):
        today = datetime.now()
        if self.value:
            birthday_date = datetime.strptime(str(self.value), '%Y-%m-%d').replace(year=today.year)
            if today > birthday_date:
                birthday_date = birthday_date.replace(year=today.year + 1)
            delta = birthday_date - today
            return delta.days
        else:
            return None

if __name__ == '__main__':
    b = Birthday('2024-10-30')
    x = b.days_to_birthday()
    print(b)
    print(x)
