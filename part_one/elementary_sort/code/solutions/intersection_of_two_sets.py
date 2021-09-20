class SolutionUnique:
    def find(self, a, b):
        a.sort(key=lambda x: x[0])
        b.sort(key=lambda x: x[0])
        count = 0
        for x_a, y_a in a:
            is_found, index = self._binary_search(b, x_a)
            if is_found:
                count += b[index][1] == y_a
        return count

    def _binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == target:
                return True, mid
            if arr[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False, None


class SolutionDuplicate:
    def find(self, a, b):
        import bisect
        a.sort(key=lambda x: x[0])
        b.sort(key=lambda x: x[0])
        count = 0
        for x_a, y_a in a:
            index = bisect.bisect_left([x_b for x_b, _ in b], x_a)
            while index < len(b) and b[index][0] == x_a:
                count += y_a == b[index][1]
                index += 1
            # while is_found and index < len(b) and b[index][0] == x_a:
            #     count += y_a == b[index][1]
            #     index += 1
        return count

    def _lower_bound(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == target:
                right = mid - 1
            elif arr[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right == -1 or left == len(arr):
            return False, None
        if arr[right] == target:
            return True, right
        if arr[left] == target:
            return True, left
        return False, None
