from typing import List


class HttpUrlException(Exception):
    ...


class InvalidProtocol(HttpUrlException):
    def __init__(self, protocol: str, possible_protocols: List[str]):
        print(f"Invalid protocol {protocol}. Protocol must be in ({', '.join(possible_protocols)})")


class InvalidDomain(HttpUrlException):
    def __init__(self):
        print(f"Domain can\'t be None or empty")


class InvalidPort(HttpUrlException):
    def __init__(self, port):
        print(f"Invalid port. Port must be integer in [1, 65535] but {port} were given")


class DelimiterNotFound(HttpUrlException):
    def __init__(self):
        print('Delimiter between protocol and domain doesn\'t found')
