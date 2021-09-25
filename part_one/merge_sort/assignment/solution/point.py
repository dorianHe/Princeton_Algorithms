class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if other.y > self.y:
            return True
        if other.y == self.y:
            return self.x < other.x
        return False

    def slope_to(self, point):
        if point.x == self.x and point.y == self.y:
            return 0
        if point.x == self.x:
            return float('inf')
        return (self.y - point.y) / (self.x - point.x)
