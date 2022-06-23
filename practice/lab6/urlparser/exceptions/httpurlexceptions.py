from typing import List


class HttpUrlExceptions(Exception):
    ...


class InvalidArgument(HttpUrlExceptions):
    def __init__(self, argument_type: str, argument: str):
        print(f'Invalid value {argument} for {argument_type}')


class InvalidProtocol(HttpUrlExceptions):
    def __init__(self, protocol: str, possible_protocols: List[str]):
        print(f"Invalid protocol {protocol}. Protocol must be in ({', '.join(possible_protocols)})")


class InvalidDomain(HttpUrlExceptions):
    def __init__(self):
        print(f"Domain can\'t be None or empty")


class InvalidPort(HttpUrlExceptions):
    def __init__(self, port):
        print(f"Invalid port. Port must be integer in [1, 65535] but {port} were given")

