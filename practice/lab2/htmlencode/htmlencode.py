from typing import Dict

from argparse import ArgumentParser
from dataclasses import dataclass

HTML_SYMBOLS: Dict[str, str] = {
    '"': '&quot;',
    '’': '&apos;',
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;'
}


@dataclass()
class ProgramArguments:
    def __init__(self, action: str, text: str):
        self.action = action
        self.text = text


def get_symbol_by_html_code(html_code: str) -> str:
    for key, value in HTML_SYMBOLS.items():
        if value == html_code:
            return key


def parse_args() -> ProgramArguments:
    parser = ArgumentParser()
    parser.add_argument('action',
                        help='encode - encode text to html;\n decode - decode html to text',
                        type=str,
                        choices=['encode', 'decode'])
    parser.add_argument('text', help='text with be encoded or decoded', type=str)

    args = parser.parse_args()
    return ProgramArguments(args.action, args.text)


def html_encode(text: str) -> str:
    encoded_html: str = ''
    for symbol in text:
        encoded_html += HTML_SYMBOLS.get(symbol) if HTML_SYMBOLS.get(symbol) else symbol
    return encoded_html


def html_decode(text: str) -> str:
    decoded_text: str = ''
    html_code: str = ''
    is_html_code = False
    for symbol in text:
        if symbol == '&':
            is_html_code = True

        if symbol == ';':
            if is_html_code:
                is_html_code = False
                symbol = get_symbol_by_html_code(html_code + ';')
                html_code = ''

        if is_html_code:
            html_code += symbol
        else:
            decoded_text += symbol
    return decoded_text


def main():
    args: ProgramArguments = parse_args()

    if args.action == 'encode':
        result = html_encode(args.text)
    else:
        result = html_decode(args.text)
    print(result)


if __name__ == '__main__':
    main()
