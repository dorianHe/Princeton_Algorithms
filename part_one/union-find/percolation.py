from typing import List
import numpy as np

class UnionFind:
    def __init__(self, row, col):
        self.root = [[(i, j) for j in range(col)] for i in range(row)]
        self.rank = [[1 for _ in range(col)] for _ in range(row)]

    def find(self, row, col):
        if (row, col) == self.root[row][col]:
            return (row, col)
        root_r, root_c = self.find(self.root[row][col][0], self.root[row][col][1])
        self.root[row][col] = (root_r, root_c)
        return self.root[row][col]
    
    def union(self, row_x, col_x, row_y, col_y):
        root_x_row, root_x_col = self.find(row_x, col_x)
        root_y_row, root_y_col = self.find(row_y, col_y)
        if (root_x_row, root_x_col) == (root_y_row, root_y_col):
            return
        if self.rank[root_x_row][root_x_col] < self.rank[root_y_row][root_y_col]:
            self.root[root_y_row][root_y_col] = self.root[root_x_row][root_x_col]
        elif self.rank[root_x_row][root_x_col] == self.rank[root_y_row][root_y_col]:
            self.rank[root_x_row][root_x_col] += 1
            self.root[root_x_row][root_x_col] = self.root[root_y_row][root_y_col]
        else:
            self.root[root_x_row][root_x_col] = self.root[root_y_row][root_y_col]

    def is_connected(self, row_x, col_x, row_y, col_y):
        return self.find(row_x, col_x) == self.find(row_y, col_y)

class Percolation:
    def __init__(self, n: int) -> List[List]:
        self.site = [[0 for _ in range(n)] for _ in range(n)]
        self.union_find = UnionFind(n, n)

    def open(self, row: int, col: int) -> None:
        if row >= len(self.site) or row < 0 or col >= len(self.site[0]) or col < 0:
            return 
        self.site[row][col] = 1
        if 0 <= row - 1 < len(self.site) and self.is_open(row - 1, col):
            self.union_find.union(row, col, row - 1, col)
        if 0 <= row + 1 < len(self.site) and self.is_open(row + 1, col):
            self.union_find.union(row, col, row + 1, col)
        if 0 <= col - 1 < len(self.site) and self.is_open(row, col - 1):
            self.union_find.union(row, col, row, col - 1)
        if 0 <= col + 1 < len(self.site) and self.is_open(row, col + 1):
            self.union_find.union(row, col, row, col + 1)

    def is_open(self, row: int, col: int) -> bool:
        if row >= len(self.site) or row < 0 or col >= len(self.site[0]) or col < 0:
            return 
        return self.site[row][col]

    def is_full(self, row: int, col: int) -> bool:
        for c in range(len(self.site[0])):
            if self.union_find.is_connected(0, c, row, col):
                return True
        return False

    def number_of_open_sites(self) -> int:
        count = 0
        for i in range(len(self.site)):
            for j in range(len(self.site[0])):
                count += self.site[i][j]
        return count

    def percolates(self) -> bool:
        for c in range(len(self.site[0])):
            if self.is_full(len(self.site) - 1, c):
                return True
        return False


class PercolationStats:
    def __init__(self, n, trials):
        self.n = n
        self.trials = trials
        self.num_open_lst = []
        for _ in range(trials):
            self.percolation = Percolation(n)
            self.test()
            if self.percolation.percolates():
                self.num_open_lst.append(self.percolation.number_of_open_sites() / self.n / self.n)
        
    def test(self) -> int:
        while not self.percolation.percolates():
            row, col = np.random.randint(0, self.n), np.random.randint(0, self.n)
            self.percolation.open(row, col)

    def mean(self) -> float:
        self.mean = np.mean(self.num_open_lst)
        return self.mean

    def stddev(self) -> float:
        self.std = np.std(self.num_open_lst)
        return self.std

    def confidence_low(self) -> float:
        return self.mean - 1.96 * self.std / self.trials

    def confidence_high(self) -> float:
        return self.mean + 1.96 * self.std / self.trials

if __name__ == '__main__':
    p = PercolationStats(2, 100000)
    print(p.mean(), p.stddev())
    print(p.confidence_low(), p.confidence_high())
