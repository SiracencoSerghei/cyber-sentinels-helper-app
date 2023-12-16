"""Processing of the directory and its subdirectories."""
from pathlib import Path
from process_file import process_file

def process_directory(directory_path: Path, sorted_folder_path: Path) -> None:
    """Recursive processing of a directory and its subdirectories."""
    #Create a list for storing folders and files for further sorting
    folders_to_sort = []
    for item in directory_path.iterdir():
        # If file, processed by a separate function
        if item.is_file():
            process_file(item, sorted_folder_path)
        elif item.is_dir():
            # Adding a folder to the list, for processing later.
            folders_to_sort.append(item)
    #Sorting out the folders in reverse order, the remaining ones have been saved in the order of deposits
    for folder in reversed(folders_to_sort):
        process_directory(folder, sorted_folder_path)
    #Deletion of empty folders
    for item in directory_path.iterdir():
        if item.is_dir() and not list(item.iterdir()):
            item.rmdir()
