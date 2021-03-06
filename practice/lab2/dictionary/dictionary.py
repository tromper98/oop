from __future__ import annotations
from typing import Dict, List, Optional
from argparse import ArgumentParser
import os
import re


class Dictionary:
    def __init__(self, dictionary: Dict[str, List[str]]):
        self.is_updated: bool = False
        self._en_dict: Dict[str, List[str]] = dictionary
        self._ru_dict: Dict[str, List[str]] = self._create_ru_dict()

    def add_translation(self, word: str, translation: str) -> None:
        if not self._has_cyrillic(word):
            self._add_translation_to_dict(self._en_dict, word, translation)
            self._add_translation_to_dict(self._ru_dict, translation, word)
        else:
            self._add_translation_to_dict(self._ru_dict, word, translation)
            self._add_translation_to_dict(self._en_dict, translation, word)
        self.is_updated = True

    def get_translation(self, word: str) -> Optional[str]:
        if self._has_translation(self._en_dict, word):
            return self._get_translation_from_dict(self._en_dict, word)

        if self._has_translation(self._ru_dict, word):
            return self._get_translation_from_dict(self._ru_dict, word)
        return

    def _create_ru_dict(self) -> Dict[str, List[str]]:
        ru_dict: Dict[str, List[str]] = dict()
        for translation, words in self._en_dict.items():
            for word in words:
                ru_dict[word] = [translation]
        return ru_dict

    def _add_translation_to_dict(self, dictionary: Dict[str, List[str]], word: str, translation: str) -> None:
        if self._has_translation(dictionary, word):
            keyword: str = self._get_dict_key(dictionary, word)
            dictionary[keyword].append(translation)
        else:
            dictionary[word] = [translation]

    @staticmethod
    def _has_cyrillic(word: str) -> bool:
        return bool(re.search(r'[а-яА-я]', word))

    @staticmethod
    def _has_translation(dictionary: Dict[str, List[str]], word: str) -> bool:
        return word.lower() in [key.lower() for key in dictionary.keys()]

    @staticmethod
    def _get_dict_key(dictionary: Dict[str, List[str]], word: str) -> str:
        keys: List[str] = [key for key in dictionary.keys()]
        return next(filter(lambda x: x.lower() == word.lower(), keys), None)

    @staticmethod
    def _get_translation_from_dict(dictionary: Dict[str, List[str]], search_word: str) -> str:
        # key переименовать
        for word, translation in dictionary.items():
            if search_word.lower() == word.lower():
                return ', '.join(translation)

    @staticmethod
    def from_file(file_path: str) -> Dictionary:
        dictionary: Dict[str, List[str]] = dict()
        with open(file_path, 'r', encoding='utf-8') as file:
            for row in file:
                sep_position = row.find(':')
                # Лучше избавиться от shadows
                phrase: str = row[:sep_position].lstrip().rstrip()
                translation: str = row[sep_position + 1:].lstrip().rstrip()
                dictionary[phrase] = translation.split(',')
        return Dictionary(dictionary)

    @staticmethod
    def create_empty() -> Dictionary:
        return Dictionary(dict())

    def save_to_file(self, file_path: str) -> None:
        with open(file_path, 'w', encoding='utf-8') as file:
            for phrase in self._en_dict.keys():
                row: str = f"{phrase}:{', '.join(self._en_dict[phrase])}\n"
                file.write(row)


def parse_command_line() -> str:
    parser = ArgumentParser()
    parser.add_argument('file_path', help='file path to dict file', type=str)

    args = parser.parse_args()
    return args.file_path


def try_to_save_dictionary(dictionary: Dictionary, file_path: str) -> None:
    if dictionary.is_updated:
        is_save = user_wants_to_save_dictionary()
        if is_save:
            dictionary.save_to_file(file_path)


def user_wants_to_save_dictionary() -> bool:
    answer = ''
    while answer not in ('yes', 'no'):
        answer = input('Сохранить изменения в словаре? (yes/no) ').lower()
    if answer == 'yes':
        return True
    return False


def ask_for_translation(phrase: str) -> str:
    print(f'Неизвестное слово "{phrase}". Введите перевод или пустую строку для отказа.')
    return input().lstrip().rstrip()


def try_to_add_translation_in_dictionary(dictionary: Dictionary, phrase: str) -> None:
    new_translation: str = ask_for_translation(phrase)
    if new_translation == '':
        print(f'Слово {new_translation} проигнорировано')
        return

    dictionary.add_translation(phrase, new_translation)
    print(f'Слово {phrase} сохранено в словаре как {new_translation}')


def read_dictionary_from_file(file_path: str) -> Optional[Dictionary]:
    if os.path.exists(file_path):
        return Dictionary.from_file(file_path)

    return None


def main() -> None:
    file_path: str = parse_command_line()
    dictionary: Dictionary = read_dictionary_from_file(file_path)
    if not dictionary:
        dictionary: Dictionary = Dictionary.create_empty()

    if not dictionary:
        return

    while True:
        phrase: str = input().lstrip().rstrip()
        if phrase == '...':
            try_to_save_dictionary(dictionary, file_path)
            break
        translation: Optional[str] = dictionary.get_translation(phrase)

        if translation:
            print(translation)
        else:
            try_to_add_translation_in_dictionary(dictionary, phrase)


if __name__ == '__main__':
    main()
