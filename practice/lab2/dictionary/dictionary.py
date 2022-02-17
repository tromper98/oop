import os.path
from typing import List

def check_input_string(input_string: str):
    ...

def read_file

def add_translate_in_file(string: str, translate_string: str, file_name: str) -> None:
    contacted_string = string + ' : ' + translate_string
    with open(os.path.abspath(file_name), 'a+', encoding='UTF-8') as file:
        file.write(contacted_string)
