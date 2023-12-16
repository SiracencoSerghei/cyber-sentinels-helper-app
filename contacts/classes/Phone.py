from Field import Field


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        if value.isdigit() and len(value) == 10:
            self.__value = value
        else:
            raise ValueError("Phone number must be a ten digit string of digits")
