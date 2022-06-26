import pytest

from exceptions import *
from httpurl import HttpUrl


def is_equal_urls(target: HttpUrl, expected: HttpUrl) -> bool:
    if target.protocol != expected.protocol:
        return False

    if target.domain != expected.domain:
        return False

    if target.port != expected.port:
        return False

    if target.document != expected.document:
        return False

    return True


def test_create_url_from_args():
    url = HttpUrl('http', 'www.domain.com', 45, '/document')
    assert url.url == 'http://www.domain.com:45/document'


def test_create_url_with_none_port():
    url = HttpUrl('https', 'www.test.ru', None, 'document')
    assert url.url == 'https://www.test.ru/document'


def test_do_not_create_url_with_invalid_protocol():
    with pytest.raises(InvalidProtocol):
        url = HttpUrl('hrrl', 'www.te.ru', 443)


def test_create_url_with_different_protocol_case():
    url1 = HttpUrl('HTTP', 'www.test1.eu')
    url2 = HttpUrl('HttP', 'www.test2.ru')
    url3 = HttpUrl('httpS', 'www.test3.com')
    assert url1.url == 'http://www.test1.eu'
    assert url2.url == 'http://www.test2.ru'
    assert url3.url == 'https://www.test3.com'


def test_append_slash_before_document():
    url1 = HttpUrl('http', 'www.google.com', document='document/test1.txt')
    url2 = HttpUrl('http', 'www.google.com', document='/document/test2.txt')
    assert url1.url == 'http://www.google.com/document/test1.txt'
    assert url2.url == 'http://www.google.com/document/test2.txt'


def test_get_url_protocol():
    url1 = HttpUrl('https', 'www.google.com')
    url2 = HttpUrl('HTTPS', 'www.ya.ru')
    url3 = HttpUrl('http', 'www.vk.com')
    url4 = HttpUrl('HTTP', 'www.def.com')
    assert url1.protocol == 'https'
    assert url2.protocol == 'https'
    assert url3.protocol == 'http'
    assert url4.protocol == 'http'


def test_get_domain():
    url1 = HttpUrl('https', 'www.google.com')
    url2 = HttpUrl('HTTPS', 'www.ya.ru')
    url3 = HttpUrl('http', 'www.vk.com', 45, '/document/text1.txt')
    url4 = HttpUrl('HTTP', 'www.def.com', document='labs/lab7.docx')
    assert url1.domain == 'www.google.com'
    assert url2.domain == 'www.ya.ru'
    assert url3.domain == 'www.vk.com'
    assert url4.domain == 'www.def.com'


def test_get_port():
    url1 = HttpUrl('https', 'www.google.com')
    url2 = HttpUrl('HTTPS', 'www.ya.ru', 5200)
    url3 = HttpUrl('http', 'www.vk.com', 45, '/document/text1.txt')
    url4 = HttpUrl('HTTP', 'www.def.com', document='labs/lab7.docx')
    assert url1.port == 443
    assert url2.port == 5200
    assert url3.port == 45
    assert url4.port == 80


def test_get_document():
    url1 = HttpUrl('https', 'www.google.com', None, '/')
    url2 = HttpUrl('HTTPS', 'www.ya.ru')
    url3 = HttpUrl('http', 'www.vk.com', 45, '/document/text1.txt')
    url4 = HttpUrl('HTTP', 'www.def.com', document='labs/lab7.docx')
    assert url1.document == '/'
    assert url2.document == '/'
    assert url3.document == '/document/text1.txt'
    assert url4.document == '/labs/lab7.docx'


def test_fail_create_url_with_invalid_ports():
    with pytest.raises(InvalidPort):
        HttpUrl('http', 'www.gog.com', -1)
    with pytest.raises(InvalidPort):
        HttpUrl('https', 'www.test.com', 0)
    with pytest.raises(InvalidPort):
        HttpUrl('https', 'www.google.com', 65536)


def test_create_httpurl_from_string():
    url1 = 'https://google.com/docs/text1.txt'
    url2 = 'HTTPS://yandex.com:70/docs/text2.txt'
    url3 = 'http://go.ru'
    url4 = 'http://dada.ua:50'

    expected1 = HttpUrl('https', 'google.com', document='docs/text1.txt')
    expected2 = HttpUrl('https', 'yandex.com', 70, 'docs/text2.txt')
    expected3 = HttpUrl('http', 'go.ru')
    expected4 = HttpUrl('http', 'dada.ua', 50)

    assert is_equal_urls(HttpUrl.from_string(url1), expected1)
    assert is_equal_urls(HttpUrl.from_string(url2), expected2)
    assert is_equal_urls(HttpUrl.from_string(url3), expected3)
    assert is_equal_urls(HttpUrl.from_string(url4), expected4)


def test_fail_create_httpurl_from_string():
    url1 = 'httr://google.com/docs/text1.txt'
    url2 = 'HTTps://yandex.com:-70/docs/text2.txt'
    url3 = 'http://go.ru:0'
    url4 = 'http://:50'

    with pytest.raises(HttpUrlExceptions):
        HttpUrl.from_string(url1)

    with pytest.raises(HttpUrlExceptions):
        HttpUrl.from_string(url2)

    with pytest.raises(HttpUrlExceptions):
        HttpUrl.from_string(url3)

    with pytest.raises(HttpUrlExceptions):
        HttpUrl.from_string(url4)
