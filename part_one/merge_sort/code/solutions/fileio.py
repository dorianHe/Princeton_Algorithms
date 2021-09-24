from abc import ABC, abstractmethod


class ReaderFactory:
    def create_reader(self, question_id):
        if question_id == 1:
            pass
        elif question_id == 2:
            reader = CountingInversionReader()
        elif question_id == 3:
            pass
        else:
            return None
        return reader


class Reader(ABC):
    @abstractmethod
    def read(self, file_path):
        pass


class CountingInversionReader(Reader):
    def read(self, file_path):
        with open(file_path, 'r') as f:
            data = f.readlines()
        data = list(map(lambda x: int(x), data[0].split()))
        return data
