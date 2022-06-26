from __future__ import annotations
from typing import Optional, Tuple

from exceptions import *

POSSIBLE_PROTOCOLS = {
    'http': 80,
    'https': 443
}

MAX_PREFIX_LENGTH: int = 8
PROTOCOL_HOST_DELIMITER_LENGTH: int = 3


class HttpUrl:
    _protocol: str
    _domain: str
    _port: Optional[int]
    _document: Optional[str]

    def __init__(self, protocol: str, domain: str, port: Optional[int] = None, document: Optional[str] = None):
        HttpUrl._validate_arguments(protocol, domain, port)

        self._protocol = protocol.lower()
        self._domain = domain
        self._port = port if protocol not in POSSIBLE_PROTOCOLS.values() else None

        if document:
            self._document = document if document[0] == '/' else '/' + document
        else:
            self._document = None

    @classmethod
    def from_string(cls, url: str) -> HttpUrl:
        protocol, domain, port, document = cls._parse_url(url)
        return HttpUrl(protocol, domain, port, document)

    @staticmethod
    def _validate_arguments(protocol: str, domain: str, port: Optional[int]):
        if protocol.lower() not in POSSIBLE_PROTOCOLS:
            raise InvalidProtocol(protocol, list(POSSIBLE_PROTOCOLS.keys()))

        if domain is None or domain == '':
            raise InvalidDomain()

        if port is not None and not HttpUrl._is_valid_port(port):
            raise InvalidPort(port)

    @staticmethod
    def _is_valid_port(port: int) -> bool:
        if not isinstance(port, int):
            return False

        if not 1 <= port <= 65535:
            return False

        return True

    @staticmethod
    def _parse_url(url: str) -> Tuple[str, str, int, str]:
        prefix: str = url[0:MAX_PREFIX_LENGTH]
        if '://' not in prefix:
            raise EmptyProtocol()

        protocol: str = prefix[:prefix.find(':')].lower()

        path: str = url[len(protocol) + PROTOCOL_HOST_DELIMITER_LENGTH:]

        host_end: int = path.find(':')
        port_end: int = path.find('/')

        if host_end > port_end and port_end != -1:
            host_end = -1

        if port_end == -1:
            port_end = len(path)

        if host_end != -1:
            host: str = path[:host_end]
            port: Optional[str] = path[host_end + 1: port_end]
            try:
                port: int = int(port)
            except ValueError:
                raise InvalidPort(port)

        else:
            host = path[:port_end]
            port = None

        document: Optional[str] = path[port_end + 1:]
        return protocol, host, port, document

    @property
    def url(self) -> str:
        url: str = f'{self._protocol}://{self._domain}'
        if self._port:
            url += f':{self._port}'
        if self._document:
            url += self._document
        return url

    @property
    def protocol(self) -> str:
        return self._protocol

    @property
    def domain(self) -> str:
        return self._domain

    @property
    def document(self) -> str:
        if not self._document:
            return '/'

        return self._document

    @property
    def port(self) -> int:
        if not self._port:
            return POSSIBLE_PROTOCOLS[self._protocol]

        return self._port
