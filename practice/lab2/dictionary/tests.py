import pytest
from dictionary import *


def test_get_dict_from_file():
    file_path = './data/test.txt'
    result = get_dict_from_file(file_path)
    expected = {'test': ['тест'], 'data': ['данные'], 'path': ['путь']}
    assert result == expected


def test_get_dict_from_empty_file():
    file_path = './data/empty.txt'
    result = get_dict_from_file(file_path)
    expected = dict()
    assert result == expected


def test_add_translate():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    dictionary.add_translate('python', 'питон')
    expected = {'data': ['данные'],
                'text': ['текст'],
                'script': ['скрипт'],
                'python': ['питон']}
    assert dictionary._dict == expected


def test_extend_translate():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    dictionary.add_translate('data', 'информация')
    expected = {'data': ['данные', 'информация'],
                'text': ['текст'],
                'script': ['скрипт']}
    assert dictionary._dict == expected


def test_get_translate():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    result = dictionary.get_translate('text')
    assert 'текст' == result


def test_none_get_translate():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    result = dictionary.get_translate('python')
    assert result is None


def test_get_capitalize_translate():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    result = dictionary.get_translate('Script')
    assert 'скрипт' == result


def test_get_upper_case_translate():
    dictionary = Dictionary(
        {'data': ['данные'],
         'text': ['текст'],
         'script': ['скрипт']})
    result = dictionary.get_translate('SCRIPT')
    assert 'скрипт' == result


def test_get_en_and_ru_dicts():
    file_path = './data/test.txt'
    en_dict = get_en_dictionary(file_path)
    ru_dict = get_ru_dictionary(file_path)

    en_expected = {
        'test': ['тест'],
        'data': ['данные'],
        'path': ['путь']}

    ru_excepted = {
        'тест': ['test'],
        'данные': ['data'],
        'путь': ['path']}
    assert en_dict._dict == en_expected
    assert ru_dict._dict == ru_excepted


def test_multi_translates_dict():
    file_path = './data/test2.txt'
    en_dict = get_en_dictionary(file_path)
    ru_dict = get_ru_dictionary(file_path)

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

    assert en_dict._dict == en_expected
    assert ru_dict._dict == ru_expected
