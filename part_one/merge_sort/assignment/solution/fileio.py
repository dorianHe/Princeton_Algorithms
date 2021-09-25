class Reader:
    @staticmethod
    def read(file_path):
        with open(file_path, 'r') as f:
            data = f.readlines()
        return list(map(lambda x: [int(x[0]), int(x[1])], list(map(lambda x: x.split(), data))))
