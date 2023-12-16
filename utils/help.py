# RED = "\033[91m"
# GREEN = "\033[92m"
# BLUE = "\033[94m"
# YELLOW = "\033[43m"
# PINK = "\033[95m"
# RESET = "\033[0m"



# def help():
#     """Print help information about available commands."""
#     print(f"{YELLOW}Available Commands:{RESET}")
#     print(f"{PINK}{'Command':<20}{'Description'}{RESET}")
#     print("-" * 40)
#     print(f"{BLUE}{'hello':<20}{'Greet the user'}{RESET}")
#     print(f"{GREEN}{'add <name> <phone>':<20}{'Add a contact with the given name and phone number(s)'}{RESET}")
#     print(f"{BLUE}{'change <name> <old_phone> <new_phone>':<20}{'Change the phone number associated with a contact'}{RESET}")
#     print(f"{GREEN}{'show <chunk_size>':<20}{'Display all contacts in the address book in chunks of specified size'}{RESET}")
#     print(f"{BLUE}{'phone <name>':<20}{'Retrieve the phone numbers associated with a contact'}{RESET}")
#     print(f"{GREEN}{'days-to-birthday <name>':<20}{'Calculate the number of days to the next birthday for a contact'}{RESET}")
#     print(f"{BLUE}{'add-birthday <name> <YYYY-MM-DD>':<20}{'Add a birthday to a contact'}{RESET}")
#     print(f"{GREEN}{'edit-birthday <name> <YYYY-MM-DD>':<20}{'Edit the birthday of a contact'}{RESET}")
#     print(f"{BLUE}{'find <search_param>':<20}{'Search for contacts based on a parameter'}{RESET}")
#     print(f"{RED}{'goodbye, close, exit, . (dot) ':<20}{'Exit the program'}{RESET}")

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
        ("hello", "Greet the user"),
        ("add <name> <phone>", "Add a contact with the given name and phone number(s)"),
        ("change <name> <old_phone> <new_phone>", "Change the phone number associated with a contact"),
        ("show <chunk_size>", "Display all contacts in the address book in chunks of specified size"),
        ("phone <name>", "Retrieve the phone numbers associated with a contact"),
        ("days-to-birthday <name>", "Calculate the number of days to the next birthday for a contact"),
        ("add-birthday <name> <YYYY-MM-DD>", "Add a birthday to a contact"),
        ("edit-birthday <name> <YYYY-MM-DD>", "Edit the birthday of a contact"),
        ("find <search_param>", "Search for contacts based on a parameter"),
        # ("goodbye, close, exit, . (dot)", "Exit the program"),
    ]

    for i, (command, description) in enumerate(rows):
        style = f"{'#1D95C4'}" if i % 2 == 0 else f"{GREEN}"
        table.add_row(command, description, style=style)

    # Print the exit command in red
    table.add_row(f"[{RED}]goodbye, close, exit, . (dot)[/]", f"[{RED}]Exit the program[/]")

    console.print(table)
