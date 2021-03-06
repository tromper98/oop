from typing import Dict, Optional

HTML_CODES: Dict[str, str] = {
    '"': '&quot;',
    '’': '&apos;',
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;'
}

MAX_HTML_CODE_LENGTH = 10


def get_html_code(html_code: str) -> Optional[str]:
    for key, value in HTML_CODES.items():
        if value == html_code:
            return key
    return


def html_encode(text: str) -> str:
    encoded_html: str = ''
    for symbol in text:
        encoded_html += HTML_CODES.get(symbol) if HTML_CODES.get(symbol) else symbol
    return encoded_html


def html_decode(text: str) -> str:
    decoded_text: str = ''
    i: int = 0
    while i < len(text):
        symbol: str = text[i]
        decoded_html_code: Optional[str] = None
        html_code: Optional[str] = None

        if symbol == '&':
            substring: str = text[i: i+MAX_HTML_CODE_LENGTH]
            pos: int = substring.find(';')

            if pos != -1:
                html_code = substring[: pos + 1]
                decoded_html_code = get_html_code(html_code)

        if decoded_html_code:
            decoded_text += decoded_html_code
            i += len(html_code)
        else:
            decoded_text += symbol
            i += 1

    return decoded_text


def choose_action() -> str:
    action: str = ''
    while action not in ('encode', 'decode'):
        action = input('Choose action encode or decode html string: ')
        action = action.lstrip().rstrip()
    return action


def main():
    text: str = ' '
    while text:
        text = input('Enter text: ')
        action = choose_action()
        if action == 'encode':
            result = html_encode(text)
        else:
            result = html_decode(text)
        print(result)


if __name__ == '__main__':
    main()
