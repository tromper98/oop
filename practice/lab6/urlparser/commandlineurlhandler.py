from typing import Callable

from httpurl import HttpUrl
from exceptions import HttpUrlException


class CommandLineUrlHandler:
    def __init__(self, output_func: Callable = print):
        self._output: Callable = output_func

    @staticmethod
    def get_user_input() -> str:
        user_input = input('Enter url: ')
        return user_input

    def print_url_info(self, url: str) -> None:
        try:
            parsed_url = HttpUrl.from_string(url)
            output = f"""
            url: {parsed_url.url}
            protocol: {parsed_url.protocol}
            domain: {parsed_url.domain}
            port: {parsed_url.port}
            document: {parsed_url.document} 
            """
            self._output(output)
        except HttpUrlException as e:
            self._output(e)


def main():
    handler = CommandLineUrlHandler()
    while True:
        url = handler.get_user_input()
        if url:
            handler.print_url_info(url)
        else:
            break


if __name__ == '__main__':
    main()
