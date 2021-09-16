# Interview Questions: Elementary Sorts


## Question 1

Intersection of two sets. Given two arrays a[] and b[], each containing $n$ distinct 2D points in the plane, design a subquadratic algorithm to count the number of points that are contained both in array a[] and array b[].



## Question 2

Permutation. Given two integer arrays of size n, design a subquadratic algorithm to determine whether one is a permutation of the other. That is, do they contain exactly the same entries but, possibly, in a different order.


## Question 3

Dutch national flag. Given an array of nnn buckets, each containing a red, white, or blue pebble, sort them by color. The allowed operations are:

    swap(i,j)swap(i, j)swap(i,j):  swap the pebble in bucket iii with the pebble in bucket jjj.
    color(i)color(i)color(i): determine the color of the pebble in bucket iii.

The performance requirements are as follows:

    At most nnn calls to color()color()color().
    At most nnn calls to swap()swap()swap().
    Constant extra space.

