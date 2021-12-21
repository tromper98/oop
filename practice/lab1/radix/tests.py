import subprocess

import pytest


def test_convert_hex_to_nine():
    params = ['python', 'radix.py', '-255', '16', '9']
    expected = -733
    res = subprocess.run(params, stdout=subprocess.PIPE)
    assert int(res.stdout) == expected


def test_convert_bin_to_ten():
    params = ['python', 'radix.py', '1000100111', '2', '10']
    expected = 551
    res = subprocess.run(params, stdout=subprocess.PIPE)
    assert int(res.stdout) == expected


def test_convert_hex_to_eight():
    params = ['python', 'radix.py', '9F5A3B', '16', '8']
    expected = 47655073
    res = subprocess.run(params, stdout=subprocess.PIPE)
    assert int(res.stdout) == expected


def test_convert_with_wrong_base_from():
    params = ['python', 'radix.py', '9F5A3B', '40', '8']
    res = subprocess.run(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert res.returncode == 1


def test_convert_with_wrong_base_to():
    params = ['python', 'radix.py', '9F5A3B', '16', '40']
    res = subprocess.run(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert res.returncode == 1