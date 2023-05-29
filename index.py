from os import walk
from pathlib import Path, PurePath
from config import start_path, result_path, result_file_name, exclude_folders, include_extensions, is_add_in_file


def get_files_list(current_path: str, exclude_folders: list):
    dirs_obj = walk(current_path)
    new_dir = next(dirs_obj)

    current_dir = new_dir[0]
    sub_folders = new_dir[1]
    files = new_dir[2]

    file_paths = []
    for folder in sub_folders:
        if (folder not in exclude_folders):
            file_paths.extend(get_files_list(
                str(Path(current_dir, folder)), exclude_folders))

    for file_path in files:
        file_paths.append(str(Path(current_dir, file_path)))
    return file_paths


def all_files_in_one(files: list, start_directory_name: str, full_result_path: str, include_extensions: list) -> None:
    for file in files:
        if (Path(file).suffix not in include_extensions):
            continue
        with open(file, 'r', encoding='utf-8') as readable_file:
            with open(full_result_path, 'a', encoding='utf-8') as writableFile:
                file_name = readable_file.name
                title = get_title(file_name, start_directory_name)

                writableFile.write(title)
                writableFile.write(readable_file.read())


def get_title(file_name: str, start_directory_name: str) -> str:
    name = file_name[file_name.find(start_directory_name):]
    line = len(name) * '-' + 14 * '-'
    return ''.join(['\n', line, '\n', '-----| ', name, ' |-----', '\n', line, '\n', '\n',])


def delete_result_file(is_add_in_file: bool, full_result_path: str) -> None:
    if (full_result_path.is_file() and not is_add_in_file):
        Path.unlink(full_result_path)


def get_start_directory_name(start_path: str) -> str:
    return Path(start_path).stem


def get_full_result_path(result_path: str, result_file_name: str) -> PurePath:
    return Path(result_path, result_file_name)


file_paths = get_files_list(start_path, exclude_folders)
start_directory_name = get_start_directory_name(start_path)
full_result_path = get_full_result_path(result_path, result_file_name)

delete_result_file(is_add_in_file, full_result_path)
all_files_in_one(file_paths, start_directory_name,
                 full_result_path, include_extensions)
