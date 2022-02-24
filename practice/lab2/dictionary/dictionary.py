import os
import shutil
from typing import Iterable, Iterator, List, Tuple, Union, TextIO
from argparse import ArgumentParser


def get_dict_file_path_from_command_line() -> str:
    parser = ArgumentParser()
    parser.add_argument('file_path', help='file path to dict file', type=str)

    args = parser.parse_args()
    return args.file_path


def open_file(file_path: str) -> TextIO:
    file_path = os.path.abspath(file_path)
    return open(file_path, 'w+', encoding='utf-8')


def close_file(file: TextIO) -> None:
    return file.close()


def create_temp_file(file_path: str) -> str:
    file_path = os.path.abspath(file_path)
    temp_file_path = os.path.abspath(file_path + '.tmp')
    shutil.copy(file_path, temp_file_path)
    return temp_file_path


def get_last_updated_time(file_path: str) -> float:
    file_path = os.path.abspath(file_path)
    return os.stat(file_path).st_mtime


def file_iterator(file: TextIO) -> Iterator[str]:
    for row in file:
        yield row


def parse_dict_string(string: str) -> Tuple[str, str]:
    sep_position = string.find(':')
    word = string[:sep_position].lstrip().rstrip()
    translate = string[sep_position + 1:].lstrip().rstrip()
    return word, translate


def get_translate(word: str, source: Iterable[str]) -> Union[str, bool]:
    for data in source:
        wd, tr = parse_dict_string(data)
        if word == wd:
            return tr
    return False


def save_translate_to_file(word: str, translate: str, file: TextIO) -> None:
    row: str = word + ' : ' + translate
    file.write(row)


def main() -> None:
    file_path = get_dict_file_path_from_command_line()
    copy_file_path = create_temp_file()
    file: TextIO = open_file(file_path)
    open_time: float = get_last_updated_time(file_path)

    user_input = input()
    lower_input: str = user_input.lower()

    found_string: Union[str, bool] = get_translate(lower_input, file_iterator(file))
    if user_input == '...':
        last_update_time = get_last_updated_time(file_path)
        if open_time == last_update_time:
            result = ''
            while result != 'y' or result != 'n':
                print('В словарь были внесены изменения. Введите y для сохранения данных '
                      'или n чтобы не сохранять изменения')
                result = input().lower()

    if found_string:
        print(found_string)
    else:
        print(f'Неизвестное слово {user_input}. Введите перевод или пустую строку для отказа')
        translate: str = input()
        if translate:
            save_translate_to_file(user_input, translate, file)



