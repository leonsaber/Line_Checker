import threading
from CsvLinePicker import LineSizeError, CsvLinePicker


class CountWorker(threading.Thread):

    # This is a thread which handles single file IO tasks
    def __init__(self, filename_list, counter, index):
        threading.Thread.__init__(self)
        self.filename_list = filename_list
        self.counter = counter
        self.thread_index = index
        self.line_picker = CsvLinePicker()

    # File positive line data picker
    def run(self):

        for filename in self.filename_list:

            with open(filename, 'r') as data_file:

                # scan file context
                for data_set in data_file:

                    # if positive line counter will be plus 1
                    try:
                        if self.line_picker.pick(data_set.split(',')):
                            self.counter[self.thread_index] += 1
                    except LineSizeError:
                        print("csv line error, not 11 columns")

