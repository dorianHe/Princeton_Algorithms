class CountingInversion:
    def __init__(self, array):
        self.count = 0
        self.input_array = array

    def count_inversions(self, array):
        self._split(array, 0, len(array)-1)

    def _split(self, array, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        self._split(array, left, mid)
        self._split(array, mid + 1, right)
        self._merge_count(array, left, mid, right)

    def _merge_count(self, array, left, mid, right):
        i, k, j = left, left, mid + 1
        copy_array = array.copy()
        while i <= mid and j <= right:
            if i < j and self.input_array[i] > self.input_array[j]:
                self.count += 1
            if copy_array[i] > copy_array[j]:
                array[k] = copy_array[j]
                j += 1
            else:
                array[k] = copy_array[i]
                i += 1
            k += 1
        while i <= mid:
            array[k] = copy_array[i]
            k += 1
            i += 1
        while j <= right:
            array[k] = copy_array[j]
            k += 1
            j += 1
