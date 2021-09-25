# Interview Questions: Priority Queues

## Question 1
**Dynamic median.** Design a data type that supports insert in logarithmic time, find-the-median in constant time, and remove-the-median in logarithmic time. 
If the number of keys in the data type is even, find/remove the lower median.

Based on a leetcode problem (295. Find Median from Data Stream). Using one max-heap and one min-heap is the optimal solution. 

## Qusestion 2
**Randomized priority queue.** Describe how to add the methods `sample()` and `delRandom()` to our binary heap implementation. The two methods return a key that 
is chosen uniformly at random among the remaining keys, with the latter method also removing that key. The `sample()` method should take 
constant time; the `delRandom()` method should take logarithmic time. Do not worry about resizing the underlying array.

If it is allowed to used `heapq`, then this `sample()` and `delRandom()` is not hard to implement. The `heapq` based `heap` uses a 0-indexed array. So by generating
a random integer and doing mod operation with the length of the array, we have the sampled index. To implement `delRandom()`, I use the same way to generate the 
sampled index, swap the sampled value with the top value of the heap and pop. The sampled value is removed. By heapifying the heap, the heap remains its feature.
The `sample()` takes constant time. swapping too. 

## Question 3
Taxicab numbers. A taxicab number is an integer that can be expressed as the sum of two cubes of positive integers in two different ways: 
`a^3 + b^3 = c^3 + d^3`. For example, 1729 is the smallest taxicab number: `9^3 + 10^3 = 1^3 + 12^3`. 
Design an algorithm to find all taxicab numbers with `a`, `b`, `c`, and `d` less than `n`.

* Version 1: Use time proportional to `n^2log n` and space proportional to `n^2`.
* Version 2: Use time proportional to `n^2log n` and space proportional to `n`.

One minor error that I might find is that 1729 is actually not the smallest taxicab number. It should be `1` ([wiki](https://en.wikipedia.org/wiki/Taxicab_number)).
