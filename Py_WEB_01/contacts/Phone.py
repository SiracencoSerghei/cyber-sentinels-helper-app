# from Field import Field
from contacts.Field import Field
class Phone(Field):
    """Class for validating and sanitizing phone numbers."""

    @staticmethod
    def is_valid_phone(value):
        """Return boolean from check."""
        return value.isdigit() and 15 >= len(value) >= 10
    @staticmethod
    def raise_value_error():
        raise ValueError("Phone number must be from 10 to 15 of digits")

    @classmethod
    def sanitize_phone_number(cls, phone):
        """Sanitize and format a phone number.

        Args:
            phone (str): The input phone number to sanitize.

        Returns:
            str: The sanitized and formatted phone number.
        """
        new_phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        return new_phone

    def __init__(self, value):
        sanitized_value = self.sanitize_phone_number(value)
        if not self.is_valid_phone(sanitized_value):
            self.raise_value_error()
        super().__init__(sanitized_value)

    def __set__(self, instance, value):
        sanitized_value = self.sanitize_phone_number(value)
        if not self.is_valid_phone(sanitized_value):
            self.raise_value_error()
        self.value = sanitized_value

    def __get__(self):
        return self.value
    
    def __str__(self):
        return self.value

if __name__ == '__main__':
    phone = Phone("+1 (555) 123-45-67-12")
    print(phone)
