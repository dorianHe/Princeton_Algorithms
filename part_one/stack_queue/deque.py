class Node:
    def __init__(self, val, pre, nxt):
        self.val = val
        self.pre = pre
        self.nxt = nxt

class Deque:
    def __init__(self):
        self.head = Node(-1, None, None)
        self.tail = Node(-1, None, None)
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.count = 0
    
    def is_empty(self) -> bool:
        return self.count == 0

    def size(self) -> int:
        return self.count

    def add_first(self, val) -> None:
        new_node = Node(val, None, None)
        next_node = self.head.nxt
        self.head.nxt = new_node
        new_node.pre = self.head
        new_node.nxt = next_node
        next_node.pre = new_node

    def add_last(self, val) -> None:
        pre_node = self.tail.pre
        new_node = Node(val, None, None)
        new_node.nxt = self.tail
        new_node.pre = pre_node
        pre_node.nxt = new_node
        self.tail.pre = new_node

    def remove_first(self) -> Node:
        return_node = self.head.nxt
        next_node = return_node.nxt
        if next_node is None:
            return 'error'
        self.head.nxt = next_node
        next_node.pre = self.head
        return return_node

    def remove_last(self) -> Node:
        return_node = self.tail.pre
        prev_node = return_node.pre
        if prev_node is None:
            return 'error'
        self.tail.pre = prev_node
        prev_node.nxt = self.tail
        return return_node
    
    def traversal(self) -> None:
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.nxt

if __name__ == '__main__':
    deque = Deque()
    deque.add_first(1)
    deque.add_first(2)
    deque.add_last(4)
    deque.add_last(3)
    deque.traversal()
    print('-' * 10)
    print('remove', deque.remove_first().val)
    print('remove', deque.remove_first().val)
    deque.traversal()
    print('remove', deque.remove_last().val)
    print('remove', deque.remove_last().val)
    deque.traversal()
    print(deque.remove_first())
    print(deque.remove_last())
