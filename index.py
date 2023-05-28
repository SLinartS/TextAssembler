import os
from pathlib import Path
from config import start_path, result_path, exclude_folders, include_extensions, is_add_in_file

def get_files_list(current_path: str, exclude_folders: list):
    dirs_obj = os.walk(current_path)
    new_dir = next(dirs_obj)

    current_dir = new_dir[0]
    sub_folders = new_dir[1]
    files = new_dir[2]

    file_paths = []
    for folder in sub_folders:
        if (folder not in exclude_folders):
            file_paths.extend(get_files_list(str(Path(current_dir, folder)), exclude_folders))

    for file_path in files:
        file_paths.append(str(Path(current_dir, file_path)))
    return file_paths


def all_files_in_one(files: list, result_path: str, include_extensions: list, is_add_in_file: bool):
    result_path_with_file = Path(result_path, './allProgramCode.txt')
    if (result_path_with_file.is_file() and not is_add_in_file):
        Path.unlink(result_path_with_file)

    for file in files:
        if (Path(file).suffix not in include_extensions):
            continue
        with open(file, 'r', encoding='utf-8') as readable_file:
            with open(result_path_with_file, 'a', encoding='utf-8') as writableFile:
                file_name = readable_file.name

                line = len(file_name) * '-' + 24 * '-'
                title = ''.join(
                    ['\n', line, '\n', '----------| ', file_name, ' |----------', '\n', line, '\n', '\n',])

                writableFile.write(title)
                writableFile.write(readable_file.read())


file_paths = get_files_list(start_path, exclude_folders)
all_files_in_one(file_paths, result_path, include_extensions, is_add_in_file)
