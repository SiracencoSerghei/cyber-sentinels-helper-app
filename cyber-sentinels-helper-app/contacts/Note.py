from Field import Field

class Note(Field):
    """class for validate note field"""

    def __init__(self, value):
        if not self.is_valid_note(value):
            raise ValueError("Note must be at least one character long")
        super().__init__(value)

    @staticmethod
    def is_valid_note(value):
        """return boolean from check"""
        return len(value.strip()) > 0

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, new_value):
        if not self.is_valid_note(new_value):
            raise ValueError("Note must be at least one character long")
        self.value = new_value
