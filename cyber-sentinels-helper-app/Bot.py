from abc import ABC, abstractmethod
from rich.console import Console
from rich.table import Table


class AbstractManager(ABC):
    @abstractmethod
    def display_info(self):
        pass


class ContactsManager(AbstractManager):
    def __init__(self, address_book):
        self.address_book = address_book

    def display_info(self):
        console = Console()
        table = Table(title="Address Book")
        # ... (rest of your display logic)