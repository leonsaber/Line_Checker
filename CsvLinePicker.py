class LineSizeError(Exception):
    pass


class LinePicker:

    def __init__(self):
        pass

    def pick(self):
        pass


class CsvLinePicker(LinePicker):

    def __init__(self):
        pass

    # judge cols length if not equals 11 will throw error
    def pick(self, line):
        if len(line) != 11:
            raise LineSizeError()

        # positive line valid conditions
        if (line[9] == '0' and
            ((not line[1] and not line[2] and line[10] != 'Clean') or
                (line[1] and line[2] and not line[10]))):

            return True

        return False
