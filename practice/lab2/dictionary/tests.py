import pytest
from dictionary import *


def test_get_dict_from_file():
    file_path = './data/test.txt'
    result = Dictionary.from_file(file_path)
    expected = {'test': ['тест'], 'data': ['данные'], 'path': ['путь']}
    assert result._en_dict == expected


def test_get_dict_from_empty_file():
    file_path = './data/empty.txt'
    result = Dictionary.from_file(file_path)
    expected = Dictionary(dict())
    assert result._en_dict == expected._en_dict


def test_add_translation():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    dictionary.add_translation('python', 'питон')
    expected = {'data': ['данные'],
                'text': ['текст'],
                'script': ['скрипт'],
                'python': ['питон']}
    assert dictionary._en_dict == expected


def test_extend_translation():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    dictionary.add_translation('data', 'информация')
    expected = {'data': ['данные', 'информация'],
                'text': ['текст'],
                'script': ['скрипт']}
    assert dictionary._en_dict == expected


def test_get_translation():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    result = dictionary.get_translation('text')
    assert 'текст' == result


def test_none_get_translation():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    result = dictionary.get_translation('python')
    assert result is None


def test_get_capitalize_translation():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    result = dictionary.get_translation('Script')
    assert 'скрипт' == result


def test_get_upper_case_translation():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    result = dictionary.get_translation('SCRIPT')
    assert 'скрипт' == result


def test_get_en_and_ru_dicts():
    file_path = './data/test.txt'
    dictionary = Dictionary.from_file(file_path)

    en_expected = {
        'test': ['тест'],
        'data': ['данные'],
        'path': ['путь']}

    ru_excepted = {
        'тест': ['test'],
        'данные': ['data'],
        'путь': ['path']}
    assert dictionary._en_dict == en_expected
    assert dictionary._ru_dict == ru_excepted


def test_multi_translations_dict():
    file_path = './data/test2.txt'
    dictionary = Dictionary.from_file(file_path)

    en_expected = {
        'data': ['данные', 'информация', 'сведения'],
        'test': ['тест', 'проверка'],
        'script': ['скрипт', 'алгоритм']
    }

    ru_expected = {
        'данные': ['data'],
        'информация': ['data'],
        'сведения': ['data'],
        'тест': ['test'],
        'проверка': ['test'],
        'скрипт': ['script'],
        'алгоритм': ['script']
    }

    assert dictionary._en_dict == en_expected
    assert dictionary._ru_dict == ru_expected


def test_append_translations_dict():
    file_path = './data/test2.txt'
    dictionary = Dictionary.from_file(file_path)
    dictionary.add_translation('test', 'тестирование')
    en_expected = {
        'data': ['данные', 'информация', 'сведения'],
        'test': ['тест', 'проверка', 'тестирование'],
        'script': ['скрипт', 'алгоритм']
    }

    ru_expected = {
        'данные': ['data'],
        'информация': ['data'],
        'сведения': ['data'],
        'тест': ['test'],
        'проверка': ['test'],
        'скрипт': ['script'],
        'алгоритм': ['script'],
        'тестирование': ['test']
    }

    assert dictionary._en_dict == en_expected
    assert dictionary._ru_dict == ru_expected


def test_get_new_translation_from_dict():
    file_path = './data/test2.txt'
    dictionary = Dictionary.from_file(file_path)
    dictionary.add_translation('script', 'порядок действий')

    ru_excepted = ', '.join(['скрипт', 'алгоритм', 'порядок действий'])
    en_expected = 'script'

    assert dictionary.get_translation('script') == ru_excepted
    assert dictionary.get_translation('порядок действий') == en_expected


def test_get_key_from_dict():
    file_path = './data/test2.txt'
    dictionary = Dictionary.from_file(file_path)

    result = Dictionary._get_dict_key(dictionary._en_dict, 'SCript')
    assert result == 'script'
