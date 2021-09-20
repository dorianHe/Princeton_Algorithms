# Interview Questions: Elementary Sorts


## Question 1

Intersection of two sets. Given two arrays `a[]` and `b[]`, each containing `n` distinct 2D points in the plane, design a subquadratic algorithm to count the number of points that are contained both in array `a[]` and array `b[]`.

Answer: 

To start with, I will also ask the interviewer for more details about this question. For example, the points are simply stored in a list with two elements representing x and y axis or they are point instances. Another question is the point x-, y-axis values are int or float. When we say a point is contained in `a[]` and `b[]`, it means that a point from `a[]` has the same x-, y-axis value as another point in `b[]`. And point one at `[4, 0]` is considered as equal to point two at `[4.0 ,0]`. Also, is there any duplications in one array. And are the duplications counted in the result?

Then I will start with the brute-force solution, which is comparing the points one by one in both arrays through nested loops. This takes O(n^2) time complexity. And I will start to optimize it. An intuitive idea is to use hash. By hashing the tuple of x and y value we use O(1) time complexity to check the existed point. But this takes extra space. What if we want a solution with space complexity of O(1)? 

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

