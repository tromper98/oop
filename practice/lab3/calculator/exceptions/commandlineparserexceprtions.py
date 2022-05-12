class CommandLineParserError(Exception):
    ...


class CommandLineInputError(CommandLineParserError):
    def __init__(self):
        super().__init__('Command line input error')

