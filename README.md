## English

## About

The application collects all the text from the files into one file.

### All settings in config.py. Copy config.example.py -> config.py

**`start_path: string`**

The path to the folder where you need to recursively search for files.

**`result_path: string`**

The path to the folder where the result file will be saved.

**`result_file_name: string`**

Name and extension of the result file.

**`exclude_folders: []`**

A list of folders to exclude from the search.

**`include_extensions: []`**

A list of file extensions from which the text will be taken.

**`is_add_in_file: bool`**

If the value is False, the result file is deleted before each restart.
Otherwise, the information is added to the end of the result file at each run.

## Russian

## О приложении

Приложение собирает весь текст из файлов в один файл.

### Все настройки в config.py. Скопировать config.example.py -> config.py

**`start_path: string`**

Путь до папки, в которой необходимо рекурсивно искать файлы.

**`result_path: string`**

Путь до папки, в которую сохранится файл результата.

**`result_file_name: string`**

Наименование и расширение файла результата.

**`exclude_folders: []`**

Список папок, которые необходимо исключить из поиска.

**`include_extensions: []`**

Список расширений файлов, из которых будет браться текст.

**`is_add_in_file: bool`**

Если указано значение False, то перед каждым перезапуском файл результата удаляется.
Иначе, информация при каждом запуске добавляется в конец файла результата.
