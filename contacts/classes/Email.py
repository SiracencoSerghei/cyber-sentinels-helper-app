import re
from Field import  Field
R = "\033[91m"
RES = "\033[0m"
class Email(Field):
    @classmethod
    def is_valid(cls, value):
        try:
            if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', value) or value == '':
                return True
        except ValueError:
            return False
    def __init__(self, value=''):
        if not Email.is_valid(value):
            print(f"{R}The email don't added to record{RES}")
            print(f'{R}Incorrect email! Please provide correct email.{RES}')
            raise ValueError(f"{R}Not valid birthday date{RES}")
        super().__init__(value)
    def __get__(self):
        return self.value

if __name__ == '__main__':
    e = Email('AZE@AZE.AZE')
    print(e.value)
