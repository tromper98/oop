from typing import Dict, List, Tuple, Optional
from argparse import ArgumentParser


class Dictionary:
    def __init__(self, dictionary: Dict[str, List[str]]):
        self.is_updated = False
        self._en_dict: Dict[str, List[str]] = dictionary
        self._ru_dict: Dict[str, List[str]] = self._get_ru_dictionary()

    def add_translate(self, word: str, translate: str) -> None:
        if self._has_translate(word):
            self._en_dict[word].append(translate)
        else:
            self._en_dict[word] = [translate]

        self._ru_dict[translate] = [word]
        self.is_updated = True

    def get_translate(self, word: str) -> Optional[str]:
        for key, translate in self._en_dict.items():
            if word.lower() == key.lower():
                return ', '.join(translate)

        for key, translate in self._en_dict.items():
            if word.lower() == key.lower():
                return ', '.join(translate)
        return

    def _has_translate(self, word: str) -> bool:
        return word.lower() in [key.lower() for key in self._en_dict.keys()]

    def _get_ru_dictionary(self) -> Dict[str, List[str]]:
        ru_dict: Dict[str, List[str]] = dict()
        for translate, words in self._en_dict.items():
            for word in words:
                ru_dict[word] = [translate]
        return ru_dict

    def save_to_file(self, file_path: str):
        with open(file_path, 'w', encoding='utf-8') as file:
            for word in self._en_dict.keys():
                row: str = f"{word}  : {', '.join(self._en_dict[word])} \n"
                file.write(row)


def parse_dict_file_path() -> str:
    parser = ArgumentParser()
    parser.add_argument('file_path', help='file path to dict file', type=str)

    args = parser.parse_args()
    return args.file_path


def parse_file_row(string: str) -> Tuple[str, List[str]]:
    sep_position = string.find(':')
    word: str = string[:sep_position].rstrip().lstrip()
    translate: str = string[sep_position + 1:].lstrip().rstrip()
    return word, translate.split(',')


def get_dict_from_file(file_path: str) -> Dict[str, List[str]]:
    dictionary: Dict[str, List[str]] = dict()
    with open(file_path, 'r', encoding='utf-8') as file:
        for row in file:
            word, translate = parse_file_row(row)
            dictionary[word] = translate
    return dictionary


def get_en_dictionary(file_path: str) -> Dictionary:
    dictionary: Dict[str, List[str]] = get_dict_from_file(file_path)
    return Dictionary(dictionary)


def get_ru_dictionary(file_path: str) -> Dictionary:
    dictionary: Dict[str, List[str]] = get_dict_from_file(file_path)
    ru_dict: Dict[str, List[str]] = dict()
    for translate, words in dictionary.items():
        for word in words:
            ru_dict[word] = [translate]
    return Dictionary(ru_dict)


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
    dictionary: Dictionary = get_en_dictionary(file_path)

    while True:
        phrase: str = input().lstrip().rstrip()

        if phrase == '...':
            close_dictionary(dictionary, file_path)
            break

        if phrase:
            translate: Optional[str] = dictionary.get_translate(phrase)
            if translate:
                print(translate)
            else:
                new_translate: str = ask_translate(phrase)
                if new_translate:
                    dictionary.add_translate(phrase, new_translate)


if __name__ == '__main__':
    main()
