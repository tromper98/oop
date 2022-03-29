import pytest

from htmlencode import *


def test_nothing_html_encode():
    source = 'Nothing encode in this string'
    result = html_encode(source)
    assert source == result


def test_html_encode():
    source = '<String> &with& "html" symbols;'
    result = html_encode(source)
    expected = '&lt;String&gt; &amp;with&amp; &quot;html&quot; symbols;'
    assert result == expected


def test_only_html_encode():
    source = '"<&>"'
    result = html_encode(source)
    expected = '&quot;&lt;&amp;&gt;&quot;'
    assert result == expected


def test_empty_string_encode():
    source = ''
    result = html_encode(source)
    assert source == result


def test_nothing_decode():
    source = 'String without html symbols'
    result = html_decode(source)
    assert source == result


def test_html_decode():
    source = '&lt;String&gt; &amp;with&amp; &quot;html&quot; symbols;'
    result = html_decode(source)
    expected = '<String> &with& "html" symbols;'
    assert result == expected


def test_only_html_decode():
    source = '&quot;&lt;&amp;&gt;&quot;'
    result = html_decode(source)
    expected = '"<&>"'
    assert result == expected


def test_empty_html_decode():
    source = ''
    result = html_decode(source)
    assert source == result


def test_html_decode_with_special_symbol():
    source = '&Test text&amp; with <some html symbols&gt;'
    result = html_decode(source)
    expected = '&Test text& with <some html symbols>'
    assert result == expected
