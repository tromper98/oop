from typing import Dict, List, Iterable, Iterator, Tuple, Optional, Union
from argparse import ArgumentParser


class Dictionary:
    def __init__(self):
        self.is_updated = False
        self._dict: Dict[str, str] = dict()

    def add_translate(self, word: str, translate: str) -> None:
        self._dict[word] = translate
        self.is_updated = True

    def get_translate(self, word: str) -> Optional[str]:
        if not self._has_translate(word):
            return None

        return self._dict[word]

    def _has_translate(self, word: str) -> bool:
        return word in self._dict.keys()

    def save_to_file(self, file_path: str):
        with open(file_path, 'w', encoding='utf-8') as file:
            for word in self._dict.keys():
                row: str = word + ' : ' + self._dict[word] + '\n'
                file.write(row)


def parse_dict_file_path() -> str:
    parser = ArgumentParser()
    parser.add_argument('file_path', help='file path to dict file', type=str)

    args = parser.parse_args()
    return args.file_path


def parse_file_row(string: str) -> Tuple[str, str]:
    sep_position = string.find(':')
    word: str = string[:sep_position].lstrip().rstrip()
    translate: str = string[sep_position + 1:].lstrip().rstrip()
    return word, translate


def get_dict_from_file(file_path: str) -> Dictionary:
    dictionary = Dictionary()
    with open(file_path, 'r', encoding='utf-8') as file:
        for row in file:
            word, translate = parse_file_row(row)
            dictionary.add_translate(word, translate)
    dictionary.is_updated = False
    return dictionary


def get_translate(dictionary: Dict[str, str], expr: str) -> Optional[str]:
    return dictionary[expr]


def close_dictionary(dictionary: Dictionary, file_path: str) -> None:
    if dictionary.is_updated:
        is_save = ask_user_save_dict()
        if is_save:
            dictionary.save_to_file(file_path)


def ask_user_save_dict() -> bool:
    answer = ''
    while answer not in ('yes', 'no'):
        answer = input('Сохранить изменения в словаре? (yes/no) ').lower()
    if answer == 'yes':
        return True
    return False


def ask_translate(phrase: str) -> str:
    print(f'Неизвестное слово "{phrase}". Введите перевод или пустую строку для отказа.')
    return input()


def main() -> None:
    file_path: str = parse_dict_file_path()
    dictionary: Dictionary = get_dict_from_file(file_path)

    while True:
        phrase: str = input()

        if phrase == '...':
            close_dictionary(dictionary, file_path)
            break

        if phrase:
            translate: Optional[str] = dictionary.get_translate(phrase.lower())
            if translate:
                print(translate)
            else:
                new_translate: str = ask_translate(phrase)
                if new_translate:
                    dictionary.add_translate(phrase, new_translate)


if __name__ == '__main__':
    main()
