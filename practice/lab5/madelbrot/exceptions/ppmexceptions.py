class PPMException(Exception):
    ...


class FileNameTypeError(PPMException):
    def __init__(self, file_name):
        print(f'file_name must be a str, but type is {type(file_name)}')


class BrightnessError(PPMException):
    def __init__(self, brightness):
        print(f'Invalid brightness value. Value must be in [1, 255] but {brightness} were given')
