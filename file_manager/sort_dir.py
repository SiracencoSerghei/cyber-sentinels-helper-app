"""Головний модуль"""
import sys
from pathlib import Path
from process_directory import process_directory

def sort_folder(folder: str) -> None:
    """ The main function of folders processing.

    Args:
        folder (str): transfer the path to folders
    """
    folder_path = Path(folder)
    # Get the parent folder where the folder will be created "sorted"
    # parent_folder = folder_path.parent
    # sorted_folder_path = parent_folder / 'sorted'
    sorted_folder_path = folder_path
    # Make sure that the "sorted" folder exists or create it.
    #The parents parameter in the mkdir method indicates that the program should automatically create all parent directories 
    #if they do not exist.
    # Parameter exist_ok allows not to generate an error if the directory already exists.
    # sorted_folder_path.mkdir(parents=True, exist_ok=True)
    process_directory(folder_path, sorted_folder_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort_dir.py <folder_path>")
    else:
        INPUT_FOLDER = sys.argv[1]
        sort_folder(INPUT_FOLDER)
    print("Script is done")


# python3 sort_dir.py ~/Desktop/мотлох