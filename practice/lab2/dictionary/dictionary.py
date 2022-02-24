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


def get_temp_file_path(file_path: str) -> str:
    return file_path + '.tmp'


def remove_temp_file(file_path: str) -> None:
    temp_file_name: str = get_temp_file_path(file_path)
    return os.remove(temp_file_name)


def create_temp_file(file_path: str) -> str:
    file_path = os.path.abspath(file_path)
    temp_file_path = get_temp_file_path(file_path)
    shutil.copy(file_path, temp_file_path)
    return temp_file_path


def get_last_updated_time(file_path: str) -> float:
    file_path = os.path.abspath(file_path)
    return os.stat(file_path).st_mtime


def replace_file_with_temp_file(file_path: str, temp_file_path: str) -> None:
    os.remove(file_path)
    os.replace(temp_file_path, file_path)


def ask_user_save_changes() -> str:
    res: str = ''
    while res not in ('y', 'n'):
        res = input('Словарь был изменен. Y - сохранить изменения N - не сохранять изменения').lower()
    return res


def open_dictionary(file_path: str) -> TextIO:
    temp_file_path = create_temp_file(file_path)
    return open_file(temp_file_path)


def close_dictionary(file_path: str, file: TextIO) -> None:
    file_path: str = os.path.abspath(file_path)
    temp_file_path: str = get_temp_file_path(file_path)
    file_update_time: float = get_last_updated_time(file_path)
    temp_file_update_time: float = get_last_updated_time(temp_file_path)

    if file_update_time == temp_file_update_time:
        file.close()
        remove_temp_file(temp_file_path)
        return

    answer: str = ask_user_save_changes()
    if answer == 'n':
        file.close()
        remove_temp_file(temp_file_path)
        return

    file.close()
    replace_file_with_temp_file(file_path, temp_file_path)


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
    file_path: str = get_dict_file_path_from_command_line()
    file: TextIO = open_dictionary(file_path)

    user_input = input()
    lower_input: str = user_input.lower()

    # found_string: Union[str, bool] = get_translate(lower_input, file_iterator(file))
    # if user_input == '...':
    #     last_update_time = get_last_updated_time(file_path)
    #         result = ''
    #         while result != 'y' or result != 'n':
    #             print('В словарь были внесены изменения. Введите y для сохранения данных '
    #                   'или n чтобы не сохранять изменения')
    #             result = input().lower()
    #
    # if found_string:
    #     print(found_string)
    # else:
    #     print(f'Неизвестное слово {user_input}. Введите перевод или пустую строку для отказа')
    #     translate: str = input()
    #     if translate:
    #         save_translate_to_file(user_input, translate, file)



