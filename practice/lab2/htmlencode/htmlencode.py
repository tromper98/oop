import sys
from typing import Dict

from argparse import ArgumentParser
from dataclasses import dataclass

HTML_SYMBOLS: Dict[str, str] = {
    '"': '&quot',
    '’': '&apos',
    '<': '&lt',
    '>': '&qt',
    '&': '&amp'
}


@dataclass()
class ProgramArgument:
    def __init__(self, action: str, text: str):
        self.action = action
        self.text = text


def parse_params() -> ProgramArgument:
    parser = ArgumentParser()
    parser.add_argument('action',
                        help='ecnode - encode text to html;\n decode - decode html to text',
                        type=str)
    parser.add_argument('text', help='text with be encoded or decoded',type=str)

    args = parser.parse_args()
    return ProgramArgument(args.action, args.text)


def validate_action(action: str) -> None:
    if action in ['encode', 'decode']:
        return
    raise ValueError(f"Invalid action. Action may be 'encode' or 'decode'")


def html_encode(text: str) -> str:
    encoded_html: str = ''
    for symbol in text:
        if symbol in HTML_SYMBOLS.keys():
            encoded_html += HTML_SYMBOLS.get(symbol)
        else:
            encoded_html += symbol
        print(encoded_html)
    return encoded_html


def html_decode(raw_html: str) -> str:
    decoded_text = raw_html
    for symbol, html_code in HTML_SYMBOLS.items():
        decoded_text = decoded_text.replace(html_code, symbol)
    return decoded_text


def main():
    args: ProgramArgument = parse_params()
    validate_action(args.action)

    if not args.text:
        print('Text is empty')
        sys.exit(0)

    if args.action == 'encode':
        result = html_encode(args.text)
    else:
        result = html_decode(args.text)
    print(result)