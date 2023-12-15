"""скрипт обробки файлів"""

from pathlib import Path
import shutil
from normalize import normalize


def process_file(file_path: Path, target_folder: Path) -> None:
    """Process a file by moving it to the target folder and renaming it."""
    file_extension = file_path.suffix[1:].lower()
    categories = {
        'images': ['jpeg', 'png', 'jpg', 'svg', 'gif', 'svg'],
        'videos': ['avi', 'mp4', 'mov', 'mkv'],
        'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx', 'html'],
        'music': ['mp3', 'ogg', 'wav', 'amr'],
        'archives': ['zip', 'gz', 'tar'],
    }
    category = None
    for cat, extensions in categories.items():
        if file_extension in extensions:
            category = cat
            break
    if category is None:
        category = 'unknown'

    # Працюем з архівами, витягуючи їх вміст
    if category == 'archives':
        # file_path.stem, щоб отримати цю основну частину імені файлу
        archive_folder_name = normalize(file_path.stem)
        archive_folder = target_folder / 'archives' / archive_folder_name
        # Розпаковуємо архів
        shutil.unpack_archive(str(file_path), str(archive_folder))
        # Переміщуємо сам архів у папку з розпакованим вмістом
        shutil.move(str(file_path), str(archive_folder / file_path.name))
        return
    new_file_name = normalize(file_path.stem) + file_path.suffix
    target_path = target_folder / category / new_file_name
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(file_path), str(target_path))
