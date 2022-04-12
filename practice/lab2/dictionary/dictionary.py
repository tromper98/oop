from __future__ import annotations
from typing import Dict, List, Tuple, Optional
from argparse import ArgumentParser
import os
import re


class Dictionary:
    def __init__(self, dictionary: Dict[str, List[str]]):
        self.is_updated: bool = False
        self._en_dict: Dict[str, List[str]] = dictionary
        self._ru_dict: Dict[str, List[str]] = self._create_ru_dict()

    def add_translate(self, word: str, translate: str) -> None:
        if not self._has_cyrillic(word):
            self._add_translate_to_dict(self._en_dict, word, translate)
            self._add_translate_to_dict(self._ru_dict, translate, word)
        else:
            self._add_translate_to_dict(self._ru_dict, word, translate)
            self._add_translate_to_dict(self._en_dict, translate, word)
        self.is_updated = True

    def get_translate(self, word: str) -> Optional[str]:
        if self._has_translate(self._en_dict, word):
            return self._get_translate_from_dict(self._en_dict, word)

        if self._has_translate(self._ru_dict, word):
            return self._get_translate_from_dict(self._ru_dict, word)
        return

    def _create_ru_dict(self) -> Dict[str, List[str]]:
        ru_dict: Dict[str, List[str]] = dict()
        for translate, words in self._en_dict.items():
            for word in words:
                ru_dict[word] = [translate]
        return ru_dict

    def _add_translate_to_dict(self, dictionary: Dict[str, List[str]], word: str, translate: str) -> None:
        if self._has_translate(dictionary, word):
            dictionary[word].append(translate)
        else:
            dictionary[word] = [translate]

    @staticmethod
    def _has_cyrillic(word: str) -> bool:
        return bool(re.search(r'[а-яА-я]', word))

    @staticmethod
    def _has_translate(dictionary: Dict[str, List[str]], word: str) -> bool:
        return word.lower() in [key.lower() for key in dictionary.keys()]

    @staticmethod
    def _get_translate_from_dict(dictionary: Dict[str, List[str]], word: str) -> str:
        for key, translate in dictionary.items():
            if word.lower() == key.lower():
                return ', '.join(translate)

    @staticmethod
    def from_file(file_path: str) -> Optional[Dictionary]:
        def parse_file_row(string: str) -> Tuple[str, List[str]]:
            sep_position = string.find(':')
            phrase: str = string[:sep_position].lstrip().rstrip()
            translate: str = string[sep_position + 1:].lstrip().rstrip()
            return phrase, translate.split(',')

        dictionary: Dict[str, List[str]] = dict()
        with open(file_path, 'r', encoding='utf-8') as file:
            for row in file:
                phrase, translate = parse_file_row(row)
                dictionary[phrase] = translate
        return Dictionary(dictionary)

    def save_to_file(self, file_path: str) -> None:
        with open(file_path, 'w', encoding='utf-8') as file:
            for phrase in self._en_dict.keys():
                row: str = f"{phrase}:{', '.join(self._en_dict[phrase])}\n"
                file.write(row)


def parse_dict_file_path() -> str:
    parser = ArgumentParser()
    parser.add_argument('file_path', help='file path to dict file', type=str)

    args = parser.parse_args()
    return args.file_path


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
    return input().lstrip().rstrip()


def add_translate_in_dict(dictionary: Dictionary, phrase: str) -> None:
    new_translate: str = ask_translate(phrase)
    if new_translate == '':
        print(f'Слово {new_translate} проигнорировано')
        return

    dictionary.add_translate(phrase, new_translate)
    print(f'Слово {phrase} сохранено в словаре как {new_translate}')


def process_phrase(dictionary: Dictionary, phrase: str) -> None:
    translate: Optional[str] = dictionary.get_translate(phrase)

    if translate:
        print(translate)
    else:
        add_translate_in_dict(dictionary, phrase)


def open_dict_from_file(file_path: str) -> Optional[Dictionary]:
    if os.path.exists(file_path):
        return Dictionary.from_file(file_path)

    print('File not found')
    return


def main() -> None:
    file_path: str = parse_dict_file_path()
    dictionary = open_dict_from_file(file_path)

    if not dictionary:
        return

    while True:
        phrase: str = input().lstrip().rstrip()
        if phrase == '...':
            close_dictionary(dictionary, file_path)
            break
        process_phrase(dictionary, phrase)


if __name__ == '__main__':
    main()
