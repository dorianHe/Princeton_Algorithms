class DutchFlag:
    def sort(self, arr):
        i, j = 0, len(arr) - 1
        k = None
        while i <= j:
            if self._color(i, arr) == 1:
                if k is None:
                    i += 1
                else:
                    self._swap(i, k, arr)
                    k += 1
                    i += 1
            elif self._color(i, arr) == 2:
                if k is None:
                    k = i
                i += 1
            elif self._color(i, arr) == 3:
                self._swap(i, j, arr)
                j -= 1
        return arr

    def _swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

    def _color(self, i, arr):
        return arr[i]
