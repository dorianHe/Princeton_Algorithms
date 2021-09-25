# Interview Questions: Hash Tables
## Question 1
4-SUM. Given an array  `a[]` of n integers, the 4-SUM problem is to determine if there exist distinct indices `i`, `j`, `k`, and `l` such that 
`a[i]+a[j]=a[k]+a[l]`. Design an algorithm for the 4-SUM problem that takes time proportional to `n^2` (under suitable technical assumptions).

**Answer:** similar to leetcode problem [18. 4Sum](https://leetcode.com/problems/4sum/). This problem asks for existance check. The leetcode one requires returning
all quadruplets and the target sum is given. The problem here requires a hashmap. The core-idea is similar to 2sum. The hashmap stores the sum and index information.

```python
from collections import defaultdict


class Solution:
    def four_sum(self, array):
        value_index_tuple_map = defaultdict(set)
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                curr_sum = array[i] + array[j]
                if curr_sum in value_index_tuple_map:
                    if i not in value_index_tuple_map[curr_sum] and j not in value_index_tuple_map[curr_sum]:
                        return True
                value_index_tuple_map[curr_sum].add(i)
                value_index_tuple_map[curr_sum].add(j)

array = [1,0,-1,0,-2,2]
s = Solution()
print(s.four_sum(array))
```

## Question 2

**Hashing with wrong hashCode() or equals().** Suppose that you implement a data type `OlympicAthlete` for use in a `java.util.HashMap`.

* Describe what happens if you override `hashCode()` but not `equals()`.
* Describe what happens if you override `equals()` but not `hashCode()`.
* Describe what happens if you override `hashCode()` but implement 
public boolean `equals(OlympicAthlete that)` instead of
public boolean `equals(Object that)`.

Looks like java-language specific, skipped for now.
