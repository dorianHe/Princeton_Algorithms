# Interview Questions: Quicksort
## Question 1
**Nuts and bolts.** A disorganized carpenter has a mixed pile of n nuts and nnn bolts. The goal is to find the corresponding pairs of nuts and bolts. 
Each nut fits exactly one bolt and each bolt fits exactly one nut. By fitting a nut and a bolt together, the carpenter can see which one is bigger 
(but the carpenter cannot compare two nuts or two bolts directly). Design an algorithm for the problem that uses at most proportional to `nlogn` compares 
(probabilistically).

**Answer**
A tricky problem. Unfortunately I can't find the original problem from Leetcode or Lintcode. A brute-force solution that takes time complexity of `O(n^2)` is easy
to find. However, optimizing time complexity to `O(nlogn)` is not simple. The solution is to use quick sort. Take a nut from nuts and split and find the matching 
bolt. Then use the matched bolt to split the nuts. Repeatly, both nuts and bolts are sorted.


## Question 2
Selection in two sorted arrays. Given two sorted arrays `a[]` and `b[]`, of lengths `n1` and `n2` and an integer `0 ≤ k < n1 + n2`, design an algorithm to find a key of 
rank `k`. The order of growth of the worst case running time of your algorithm should be `logn`, where `n = n1 + n2`.

* Version 1: n1=n2 (equal length arrays) and k=n/2 (median).
* Version 2: k=n/2 (median).
* Version 3: no restrictions.

**Answer**
I dont't really understand the meaning of a key of rank `k`.

## Question 3
Decimal dominants. Given an array with `n` keys, design an algorithm to find all values that occur more than `n/10` times. The expected running time of your 
algorithm should be linear.

**Answer**
Since the expected running time is linear, the data structure of hashmap must be used here. Otherwise, a sort based solution with time complexity of `O(nlogn)` is
also intuitive. 
