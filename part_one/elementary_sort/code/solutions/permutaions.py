from collections import Counter


class HashmapPermutaion:
    def is_permutation(self, a, b) -> bool:
        a_counter = Counter(a)
        b_counter = Counter(b)
        return a_counter == b_counter


class SortPermutation:
    def is_permutation(self, a, b) -> bool:
        a.sort()
        b.sort()
        return a == b

