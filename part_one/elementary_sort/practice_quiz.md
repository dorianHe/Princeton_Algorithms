# Interview Questions: Elementary Sorts


## Question 1

Intersection of two sets. Given two arrays `a[]` and `b[]`, each containing `n` distinct 2D points in the plane, design a subquadratic algorithm to count the number of points that are contained both in array `a[]` and array `b[]`.

Answer: 

To start with, I will also ask the interviewer for more details about this question. For example, the points are simply stored in a list with two elements representing x and y axis or they are point instances. Another question is the point x-, y-axis values are int or float. When we say a point is contained in `a[]` and `b[]`, it means that a point from `a[]` has the same x-, y-axis value as another point in `b[]`. And point one at `[4, 0]` is considered as equal to point two at `[4.0 ,0]`. Also, is there any duplications in one array? And are the duplications counted in the result? Furthermore, are the x values or y values unique.

Then I will start with the brute-force solution, which is comparing the points one by one in both arrays through nested loops. This takes O(n^2) time complexity. And I will start to optimize it. An intuitive idea is to use hash. By hashing the tuple of x and y value we use O(1) time complexity to check the existed point. But this takes extra space. What if we want a solution with space complexity of O(1)? 

If all x values in array `a` and `b` are unique. Then we can sort both arrays by the x-value then use a binary search to find the possible same x-value. If there exists, then check whether the y-values are the same. This method takes `O(n logn)` time complexity becasue we need to go through all the points in `a` and for each point binary search it takes `O(log n)`.

If there is no assumption on the unique x-value, we can still solve this problem by sorting and binary search. We just no longer look for the exact value but the lower bound in array `b` of the target value from `a`. After finding it, we increase the index and check whether the x, y values are still the same. In this solution, the worst-case time complexity is `O(n^2)`, which means that `a` and `b` storing one same x, y value.

## Question 2

Permutation. Given two integer arrays of size `n`, design a subquadratic algorithm to determine whether one is a permutation of the other. That is, do they contain exactly the same entries but, possibly, in a different order.


## Question 3

Dutch national flag. Given an array of nnn buckets, each containing a red, white, or blue pebble, sort them by color. The allowed operations are:

    swap(i,j):  swap the pebble in bucket i with the pebble in bucket j.
    color(i): determine the color of the pebble in bucket i.

The performance requirements are as follows:

    At most n calls to color().
    At most n calls to swap().
    Constant extra space.

