

from rich.console import Console
from rich.table import Table

YELLOW = "#FFFF00"
PINK = "#FF00FF"
RESET = "#FFFFFF"
BLUE = "#0000FF"
GREEN = "#00FF00"
RED = "#FF0000"

console = Console()

def help():
    """Print help information about available commands."""
    table = Table(show_header=True, header_style=f"bold {YELLOW}")
    table.add_column("Command", width=30)
    table.add_column("Description", style=f"{RESET}")

    rows = [
        ("help", "Unleash the wisdom of available commands"),
        ("add-contact", "Summon a new contact to your address book"),
        ("add-note", "Inscribe a new note into the Book of Notes"),
        ("add-todo", "Enchant your to-do list with a new task"),
        ("edit", "Modify the essence of a contact, note, or task"),
        ("find", "Embark on a quest to discover contacts, notes, or tasks"),
        ("delete", "Banish a contact, note, or task from your realm"),
        ("show-contact", "Reveal the secrets of a specific contact"),
        ("show-notes", "Unfold the scrolls containing your mystical notes"),
        ("show-todos", "Summon a vision of your enchanted to-do list"),
        ("hello", "Greet the magical realm with a friendly salutation"),
        ("days-to-birthday", "Calculate the days until the next magical birthday"),
        ("file-manager", "Navigate the enchanted file manager")
    ]

    for i, (command, description) in enumerate(rows):
        style = f"{'#1D95C4'}" if i % 2 == 0 else f"{GREEN}"
        table.add_row(command, description, style=style)

    # Print the exit command in red
    table.add_row(f"[{RED}]goodbye, close, exit, . (dot)[/]", f"[{RED}]Exit the program[/]")

    console.print(table)