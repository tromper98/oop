from __future__ import annotations
from typing import Optional

from

POSSIBLE_PROTOCOLS = {
    'http': 80,
    'https': 443
}


class HttpUrl:
    _protocol: str
    _domain: str
    _port: Optional[int]
    _document: Optional[str]

    def __init__(self, protocol: str, domain: str, port: Optional[int], document: Optional[str] = None):

        self._protocol = protocol
        self._domain = domain
        self._port = port if protocol not in POSSIBLE_PROTOCOLS.values() else None
        self._document = document if document[0] == '/' else '/' + document

    @classmethod
    def from_string(cls, url: str) -> HttpUrl:
        ...

    def _parse_url(self, url: str):
        ...

    @property
    def url(self) -> str:
        url: str = f'{self._protocol}://{self._domain}'
        if self._port:
            url += f':{self._port}'
        url += self._document
        return url

    @property
    def domain(self) -> str:
        return self._domain

    @property
    def document(self) -> str:
        return self._document

    @property
    def port(self) -> int:
        if not self._port:
            return POSSIBLE_PROTOCOLS[self._protocol]

        return self._port
