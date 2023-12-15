
class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str(self):
        return str(self.value)
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
