class HttpUrlExceptions(Exception):
    ...


class InvalidArgument(HttpUrlExceptions):
    def __init__(self, argument_type: str, argument: str):
        print(f'Invalid value {argument} for {argument_type}')
