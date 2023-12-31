from contacts.Field import Field

class Status(Field):
    """A class representing the status of a Record in Address Book."""

    VALID_STATUSES = ["family", "work", "friends", "neighbor", "classmate", "colleague"]

    def __init__(self, value=None):
        if not self.is_valid_status(value):
            raise ValueError("Invalid status")
        super().__init__(value)

    @staticmethod
    def is_valid_status(value):
        """Check if the status is valid."""
        return value.lower() in Status.VALID_STATUSES


    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, new_value):
        if not self.is_valid_status(new_value):
            raise ValueError("Invalid status")
        self.value = new_value

if __name__ == "__main__":
    # Example usage:
    status = Status("work")
    print(status.value)