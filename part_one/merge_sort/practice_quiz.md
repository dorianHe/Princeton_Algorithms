# Interview Questions: Mergesort

## Question 1

Merging with smaller auxiliary array. Suppose that the subarray `a[0]` to `a[n−1]` is sorted and the subarray `a[n]` to `a[2∗n−1]` is sorted. How can you merge the two subarrays so that `a[0]` to `a[2∗n−1]` is sorted using an auxiliary array of length `n` (instead of `2n`)?

To start with, I will ask for more details about the two subarrays. For example, I would ensure that both subarrays have same sorting order and store (both descending or both ascending) numerical values in int or float type. Because if one array stores numbers and another stores strings or chars in alphabetic order then the merge won't make any sense without further information. Also we need to assume that the memory usage of the merged sorted array is not considered as space cost.

Now let's assume both array store numerical values in ascending order. My solution would be using two pointers initially pointing at the first element of both array, respectively. Then the smaller one is stored in the auxiliary array and move the corresponding pointer one-step forward. I will keep this process until the auxiliary array is full. Then move the elements from auxiliary to final result array and empty the auxiliary array. Keep this process until one pointer reaches its end. If another array still have non-visited elements, then move all of them to the auxiliary array.

This problem actually reminds me of another problem which asks to sort many numbers (e.g. 10GB) using limited memory space (e.g. 1G). And the solution requires a fix-size heap (also 1GB) in memory. We don't need a heap in this problem because both arrays are sorted. We just need to compare and move the pointers.

## Question 2

Counting inversions. An inversion in an array `a` is a pair of entries `a[i]` and `a[j]` such that `i<j` but `a[i]>a[j]`. Given an array, design a linearithmic algorithm to count the number of inversions.


## Question 3

Shuffling a linked list. Given a singly-linked list containing `n` items, rearrange the items uniformly at random. Your algorithm should consume a logarithmic (or constant) amount of extra memory and run in time proportional to `nlogn` in the worst case. 
