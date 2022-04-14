import pytest
from urlparser import *


def assert_parsed_urls(target: ParsedURL, excepted: ParsedURL) -> bool:
    if target.protocol == excepted.protocol \
            and target.host == excepted.host \
            and target.port == excepted.port \
            and target.document == excepted.document:
        return True
    return False


def test_valid_url():
    url = 'http://www.google.com:80/search/results'
    parsed_url = parse_url(url)
    excepted = ParsedURL(
        'http',
        'www.google.com',
        80,
        'search/results')
    assert assert_parsed_urls(parsed_url, excepted)


def test_url_without_docs():
    url = 'http://www.google.com:80'
    parsed_url = parse_url(url)
    excepted = ParsedURL(
        'http',
        'www.google.com',
        80,
        ''
        )
    assert assert_parsed_urls(parsed_url, excepted)


def test_url_without_port():
    url = 'https://www.vk.com'
    parsed_url = parse_url(url)
    expected = ParsedURL(
        'https',
        'www.vk.com',
        443,
        ''
    )
    assert assert_parsed_urls(parsed_url, expected)


def test_url_with_wrong_port():
    url = 'ftp://wwww.test.com:-100'
    parsed_url = parse_url(url)
    assert parsed_url is None


def test_url_with_zero_port():
    url = 'ftp://wwww.test.com:0'
    parsed_url = parse_url(url)
    assert parsed_url is None


def test_url_without_host():
    url = 'http:///docs/text.txt'
    parsed_url = parse_url(url)
    assert parsed_url is None


def test_url_with_empty_host():
    url = 'http://'
    parsed_url = parse_url(url)
    assert parsed_url is None


def test_url_with_wrong_protocol():
    url = 'httttp://www.google.com'
    parsed_url = parse_url(url)
    assert parsed_url is None


def test_empty_url():
    url = ''
    parsed_url = parse_url(url)
    assert parsed_url is None


def test_url_with_port_1():
    url = 'ftp://www.download.com:1/docs/text.zip'
    parsed_url = parse_url(url)
    excepted = ParsedURL(
        'ftp',
        'www.download.com',
        1,
        'docs/text.zip'
        )
    assert assert_parsed_urls(parsed_url, excepted)


def test_url_with_port_65535():
    url = 'ftp://www.download.com:65535/docs/text.zip'
    parsed_url = parse_url(url)
    excepted = ParsedURL(
        'ftp',
        'www.download.com',
        65535,
        'docs/text.zip'
        )
    assert assert_parsed_urls(parsed_url, excepted)


def test_url_with_001_port():
    url = 'https://www.google.com:001/'
    parsed_url = parse_url(url)
    assert parsed_url is None


def test_url_capitalize_protocol():
    url = 'Https://www.vk.com/'
    parsed_url = parse_url(url)
    excepted = ParsedURL(
        'https',
        'www.vk.com',
        443,
        ''
        )
    assert assert_parsed_urls(parsed_url, excepted)


def test_url_where_colon_in_docs():
    url = 'HTtp://localhost/ddd:33'
    parsed_url = parse_url(url)
    expected = ParsedURL(
        'http',
        'localhost',
        80,
        'ddd:33'
    )
    assert assert_parsed_urls(parsed_url, expected)
