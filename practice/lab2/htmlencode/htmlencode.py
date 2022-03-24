from typing import Dict, Optional

HTML_SYMBOLS: Dict[str, str] = {
    '"': '&quot;',
    '’': '&apos;',
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;'
}

#Программа должна брать данные из input
def get_html_code(html_code: str) -> Optional[str]:
    for key, value in HTML_SYMBOLS.items():
        if value == html_code:
            return key
    return


def html_encode(text: str) -> str:
    encoded_html: str = ''
    for symbol in text:
        encoded_html += HTML_SYMBOLS.get(symbol) if HTML_SYMBOLS.get(symbol) else symbol
    return encoded_html


def html_decode(text: str) -> str:
    def decode_html_code() -> Optional[str]:
        pos: int = text.find(';', i)
        if pos == -1:
            return None
        else:
            html_code: str = text[i: pos + 1]
            decoded_html: Optional[str] = get_html_code(html_code)
            return decoded_html

    decoded_text: str = ''
    i: int = 0
    while i < len(text):
        symbol: str = text[i]

        if symbol == '&':
            pos: int = text.find(';', i)
            decoded_html: Optional[str] = decode_html_code()
            if decoded_html:
                decoded_text += decoded_html
                i = pos + 1
            else:
                decoded_text += symbol
                i += 1

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
