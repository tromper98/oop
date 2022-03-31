import os
import shutil
import sys
from typing import Iterable, Iterator, Tuple, Optional, TextIO
from argparse import ArgumentParser


def parse_dict_file_path() -> str:
    parser = ArgumentParser()
    parser.add_argument('file_path', help='file path to dict file', type=str)

    args = parser.parse_args()
    return args.file_path


def open_file(file_path: str) -> TextIO:
    file = open(file_path, 'r+', encoding='utf-8')
    return file


def get_temp_file_path(file_path: str) -> str:
    return file_path + '.tmp'


def create_temp_file(file_path: str) -> str:
    temp_file_path = get_temp_file_path(file_path)
    if not os.path.isfile(file_path):
        open(file_path, 'w', encoding='utf-8').close()
    return shutil.copy2(file_path, temp_file_path)


def get_file_last_updated_time(file_path: str) -> float:
    return os.stat(file_path).st_mtime


def replace_file_with_temp_file(file_path: str, temp_file_path: str) -> None:
    os.remove(file_path)
    os.replace(temp_file_path, file_path)


def ask_user_save_changes() -> str:
    res: str = ''
    while res not in ('y', 'n'):
        print('В словарь были внесены изменения. Введите y для сохранения данных '
              'или n чтобы не сохранять изменения')
        res = input().lower()
    return res


def open_dictionary(file_path: str) -> TextIO:
    temp_file_path = create_temp_file(file_path)
    return open_file(temp_file_path)


def close_dictionary(file_path: str, file: TextIO) -> None:
    temp_file_path: str = get_temp_file_path(file_path)
    file_update_time: float = get_file_last_updated_time(file_path)
    temp_file_update_time: float = get_file_last_updated_time(temp_file_path)

    if file_update_time == temp_file_update_time:
        file.close()
        os.remove(temp_file_path)
        return

    answer: str = ask_user_save_changes()
    if answer == 'n':
        file.close()
        os.remove(temp_file_path)
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


def find_translate_in_source(word: str, source: Iterable[str]) -> Optional[str]:
    for data in source:
        wd, tr = parse_dict_string(data)
        if word == wd:
            return tr
    return None


def save_translate_to_file(word: str, translate: str, file: TextIO) -> None:
    row: str = word + ':' + translate + '\n'
    file.write(row)
    file.seek(0)


def get_translate(word: str) -> Optional[str]:
    print(f'Неизвестное слово {word}. Введите перевод или пустую строку для отказа')
    return input()


def main() -> None:
    file_path: str = parse_dict_file_path()
    file: TextIO = open_dictionary(file_path)

    while True:
        user_input = input()
        lower_input: str = user_input.lower()

        if user_input == '...':
            close_dictionary(file_path, file)
            sys.exit(0)

        if user_input:
            translate: Optional[str] = find_translate_in_source(lower_input, file_iterator(file))
            if translate:
                print(translate)
            else:
                new_translate: str = get_translate(user_input)
                if new_translate:
                    save_translate_to_file(user_input, new_translate, file)


if __name__ == '__main__':
    main()
