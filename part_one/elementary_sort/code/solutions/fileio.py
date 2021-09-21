from abc import ABC, abstractmethod


class ReaderFactory:
    def create_reader(self, question_id):
        if question_id == 1:
            reader = IntersectionReader()
        elif question_id == 2:
            reader = PermutationReader()
        else:
            return None
        return reader


class Reader(ABC):
    @abstractmethod
    def read(self, file_path):
        pass


class PermutationReader(Reader):
    def read(self, file_path):
        with open(file_path, 'r') as f:
            data = f.readlines()
            a = list(map(lambda x: int(x), data[0].split()))
            b = list(map(lambda x: int(x), data[1].split()))
        return a, b


class IntersectionReader(Reader):
    def read(self, file_path):
        with open(file_path, 'r') as f:
            data = f.readlines()
            x_a = list(map(lambda x: int(x), data[0].split()))
            y_a = list(map(lambda x: int(x), data[1].split()))
            x_b = list(map(lambda x: int(x), data[2].split()))
            y_b = list(map(lambda x: int(x), data[3].split()))
        return [(x, y) for x, y in zip(x_a, y_a)], [(x, y) for x, y in zip(x_b, y_b)]
