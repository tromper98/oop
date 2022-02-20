import subprocess

import pytest


def test_crypt_input_file():
    params = ['python', 'crypt.py', 'secret.bin', 'temp_bin', 127]
    expected = ''
    res = subprocess.run(params, stdout=subprocess,PIPE)
