class Reader:
    @staticmethod
    def read(file_path):
        with open(file_path, 'r') as f:
            data = f.readlines()
            x_a = list(map(lambda x: int(x), data[0].split()))
            y_a = list(map(lambda x: int(x), data[1].split()))
            x_b = list(map(lambda x: int(x), data[2].split()))
            y_b = list(map(lambda x: int(x), data[3].split()))
        return [(x, y) for x, y in zip(x_a, y_a)], [(x, y) for x, y in zip(x_b, y_b)]
