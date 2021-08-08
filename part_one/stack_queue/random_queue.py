import numpy as np
from collections import Counter

class RandomizedQueue:
    def __init__(self, size = 10):
        self.count = 0
        self._a = [None for _ in range(size)]
        self.head = size - 1
        self.tail = self.head
    
    def is_empty(self):
        return self.count == 0

    def enqueue(self, value):
        self._a[self.head] = value
        self.head -= 1
        if self.head == -1:
            self.head = len(self._a) - 1
            self.tail += len(self._a)
            self._a = [None for _ in range(len(self._a))] + self._a

    def dequeue(self):
        index = np.random.randint(self.head + 1, self.tail + 1)
        value = self._a[index]
        self._a[index], self._a[self.tail] = self._a[self.tail], self._a[index]
        self._a.pop()
        self.tail -= 1
        return value

    def sample(self):
        return self._a[np.random.randint(self.head + 1, self.tail + 1)]


if __name__ == '__main__':
    random_queue = RandomizedQueue(2)
    random_queue.enqueue(1)
    random_queue.enqueue(2)
    random_queue.enqueue(3)
    random_queue.enqueue(4)
    print(random_queue.dequeue())
    print(random_queue.dequeue())
    print(random_queue.dequeue())
    print(random_queue.dequeue())
    print(random_queue._a)
    print(random_queue.head, random_queue.tail)
    print('-' * 10)
    random_queue.enqueue(1)
    random_queue.enqueue(2)
    random_queue.enqueue(3)
    random_queue.enqueue(4)
    print(random_queue._a)
    print(random_queue.head, random_queue.tail)
