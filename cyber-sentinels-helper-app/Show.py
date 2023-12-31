
from rich.console import Console
from rich.table import Table

class Show:
    @staticmethod
    def show_records(book):
        """Display all contacts in the address book.

        Returns:
            None
        """
        console = Console()
        table = Table(title="Address Book")
        first_record = next(iter(book.data.values()), None)

        record_attributes = list(first_record.__dict__.keys())
        print(first_record)
        print(record_attributes)
        # Add columns dynamically based on the attributes
        for attribute in record_attributes:
            column_name = attribute.capitalize()  # Convert attribute name to title case
            table.add_column(column_name, style="blue", justify="center", min_width=10, max_width=30)

        for _, record in book.items():
            # Get attribute values dynamically
            row_data = []
            for attr in record_attributes:
                value = getattr(record, attr)

                # Check if the value is printable
                if hasattr(value, '__iter__') and not isinstance(value, str):
                    # If it's an iterable (like a list or tuple), join its elements
                    row_data.append("; ".join(map(str, value)))
                else:
                    # Otherwise, convert the value to a string
                    row_data.append(str(value))

            table.add_row(*row_data)

        console.print(table)

if __name__ == "__main__":
    print("Loading Show...")
    from contacts.AddressBook import AddressBook
    book = AddressBook.load_json_from_file("../outputs/address_book.json")
    # print(book)
    # for nam, record in book.items():
    #     print(nam)
    #     print("==============")
    #     print(record)
    #     print("+++++++++++++++++++++++++++++++++++")
    # book.show_records(book)
    req = book.find('333')
    book.show_records(req)
    # rec = book.find("ser")
    # book.show_records(rec)
