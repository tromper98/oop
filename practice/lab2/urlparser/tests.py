import pytest
from urlparser import *


def test_valid_url():
    url = 'http://wwww.google.com:80/search/results'
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is True


def test_url_without_docs():
    url = 'http://wwww.google.com:80'
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is True


def test_url_without_port():
    url = 'https://www.vk.com'
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is True


def test_url_with_wrong_port():
    url = 'ftp://wwww.test.com:-100'
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is False


def test_url_with_zero_port():
    url = 'ftp://wwww.test.com:0'
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is False


def test_url_without_host():
    url = 'http:///docs/text.txt'
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is False


def test_url_with_empty_host():
    url = 'http://'
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is False


def test_url_with_wrong_protocol():
    url = 'httttp://www.google.com'
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is False


def test_empty_url():
    url = ''
    parsed_url = parse_url(url)
    assert validate_url(parsed_url) is False
