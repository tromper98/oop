from typing import Dict, Optional

PROTOCOLS: Dict[str, int] = {
    'http': 80,
    'https': 443,
    'ftp': 21}


class ParsedURL:
    def __init__(self, url: str, protocol: str, host: str, port: str, document: str):
        self.url = url
        self.protocol = protocol
        self.host = host
        self.port = port
        self.document = document



def parse_url(url: str) -> ParsedURL:
    substring: str = url[0:8]

    if '://' not in substring:
        protocol: str = ''
    else:
        protocol: str = substring[:substring.find(':')]

    sub_url = url[len(protocol) + 3:]

    slash_pos = sub_url.find('/')
    if slash_pos == -1:
        host: str = sub_url
    else:
        host: str = sub_url[:slash_pos]

    colon_pos: int = host.find(':')
    if colon_pos == -1:
        port: str = ''
    else:
        port = host[colon_pos + 1:]
        host: str = host[:colon_pos]

    document: Optional[str] = sub_url[slash_pos + 1:] if slash_pos != -1 else ''

    return ParsedURL(url, protocol,  host, port, document)


def validate_url(parsed_url: ParsedURL) -> bool:
    if parsed_url.protocol.lower() not in PROTOCOLS.keys():
        return False

    if not parsed_url.host:
        return False

    if parsed_url.port:
        if not parsed_url.port.isdigit():
            return False

        if 1 > int(parsed_url.port) or int(parsed_url.port) < 65355:
            return False

    return True


def print_parsed_url(parsed_url: ParsedURL) -> None:
    output_string: str = f"""
        {parsed_url.url}
        HOST: {parsed_url.host}
        PORT: {parsed_url.port if parsed_url.port != '' else PROTOCOLS.get(parsed_url.protocol)}
        DOC: {parsed_url.document}
    """
    print(output_string)


def main():
    while True:
        url: str = input('Enter URL: ')
        if url:
            parsed_url: ParsedURL = parse_url(url)
            is_url: bool = validate_url(parsed_url)
            if is_url:
                print_parsed_url(parsed_url)
            else:
                print('Invalid URL')
        else:
            break


if __name__ == '__main__':
    main()
