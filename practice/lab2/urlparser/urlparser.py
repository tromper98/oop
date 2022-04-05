from typing import Dict, Optional, Union

PROTOCOLS: Dict[str, int] = {
    'http': 80,
    'https': 443,
    'ftp': 21}

MAX_PROTOCOL_LENGTH: int = 8


class ParsedURL:
    #Почему port - str?
    def __init__(self, protocol: str, host: str, port: int, document: str):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.document = document

    @property
    def url(self) -> str:
        url: str = f'{self.protocol}://{self.host}:{self.port}'
        url += f'/{self.document}' if self.document else ''
        return url


def parse_url(url: str) -> Optional[ParsedURL]:
    prefix: str = url[0:MAX_PROTOCOL_LENGTH] #Магическое число, переменную можно назвать prefix
    if '://' not in prefix:
        protocol: str = ''
    else:
        protocol: str = prefix[:prefix.find(':')].lower()

    if protocol not in PROTOCOLS.keys():
        return

    path: str = url[len(protocol) + len('://'):] #Не понятно что такое sub_url и что такое 3

    host_end: int = path.find(':') #Не понятно о каком слэше идет речь
    port_end: int = path.find('/')

    if port_end == -1:
        port_end = len(path)

    if host_end != -1:
        host: str = path[:host_end]
        port: Optional[str] = path[host_end + 1: port_end]
    else:
        host = path[:port_end]
        port = PROTOCOLS.get(protocol)

    if len(host) == 0:
        return

    if not validate_port(port):
        return

    document: Optional[str] = path[port_end + 1:]

    return ParsedURL(protocol,  host, int(port), document)


#Валидация должна быть частью парсинга либо валидацию поместить в конструктор ParsedURL
def validate_port(port: Union[str, int]) -> bool:
    if isinstance(port, str):
        if not port.isdigit():
            return False

        if port.startswith('0'):
            return False

        port = int(port)

    if port < 1 or port > 65355:
        return False

    #Ошибки там, где их не тестируют
    #Не писать код, если для него не написан тест
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
            parsed_url: Optional[ParsedURL] = parse_url(url)
            if parsed_url:
                print_parsed_url(parsed_url)
            else:
                print('Invalid URL')
        else:
            break


if __name__ == '__main__':
    main()
#Порт 001 должен быть невалидным
#Порт 65535 должен быть валидным
#Неправильно определил c Https