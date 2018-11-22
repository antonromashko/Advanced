import os
import glob


class LogReader:
    def __init__(self, path=os.getcwd(), mask='*.log'):
        self.files_lines = []
        self.path = path
        self.mask = mask
        self.filtered_files = sorted(glob.glob(self.mask))

    def __iter__(self):
        for q in self.get_lines():
            yield q

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.files_lines = []

    def get_lines(self):
        for file_name in self.filtered_files:
            with open(file_name, 'r') as fn:
                self.files_lines.extend(fn.read().splitlines())
        return sorted(self.files_lines)

    @property
    def files(self):
        yield from self.filtered_files


with LogReader() as lg:
    for i in lg.files:
        print(i)

    for e in lg:
        print(e)
