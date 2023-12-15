"""Головний модуль"""
import sys
from pathlib import Path
from process_directory import process_directory

def sort_folder(folder: str) -> None:
    """ Головна функція обробки папки

    Args:
        folder (str): передаем шлях до папки
    """
    folder_path = Path(folder)
    # Отримуємо батьківську папку, де буде створена папка "sorted"
    # parent_folder = folder_path.parent
    # sorted_folder_path = parent_folder / 'sorted'
    sorted_folder_path = folder_path
    # Переконаемось, що папка "sorted" існує або створім її
    #Параметр parents в методі mkdir вказує, що програма повинна
    # автоматично створити всі батьківські директорії, якщо вони не існують.
    # Параметр exist_ok дозволяє не генерувати помилку, якщо директорія вже існує.
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