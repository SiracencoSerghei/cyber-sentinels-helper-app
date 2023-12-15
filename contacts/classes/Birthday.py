from Field import Field
from datetime import datetime


class Birthday(Field):
    def value(self, value):
        if datetime.strptime(value, '%d.%m.%Y'):
            self.__value = value
        else:
            raise ValueError