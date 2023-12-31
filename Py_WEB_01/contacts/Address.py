from contacts.Field import Field

class Address(Field):
    """Class for validating and storing addresses."""

    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid address")
        super().__init__(value)

    def __get__(self, instance, owner):
        # Implement how to get the address value
        return instance._address  # Assuming your address attribute is named _address

    def __set__(self, instance, new_value):
        # Implement how to set the address value
        if not self.is_valid(new_value):
            raise ValueError("Invalid address")
        self._address = new_value

    @staticmethod
    def is_valid(value):
        # maybe need to do like record with fields like street, house, ....etc
        # For simplicity, this example assumes any non-empty string is a valid address
        return bool(value)

# Example usage:
if __name__ == '__main__':
    address_field = Address("123 Main St")
    print(address_field)