# Interview Questions: Mergesort (ungraded)

## Question 1

Merging with smaller auxiliary array. Suppose that the subarray a[0]\mathtt{a[0]}a[0] to a[n−1]\mathtt{a[n-1]}a[n−1] is sorted and the subarray a[n]\mathtt{a[n]}a[n] to a[2∗n−1]\mathtt{a[2*n-1]}a[2∗n−1] is sorted. How can you merge the two subarrays so that a[0]\mathtt{a[0]}a[0] to a[2∗n−1]\mathtt{a[2*n-1]}a[2∗n−1] is sorted using an auxiliary array of length nnn (instead of 2n2n2n)?

## Question 2

Counting inversions. An inversion in an array a[ ]a[\,]a[] is a pair of entries a[i]a[i]a[i] and a[j]a[j]a[j] such that i<ji < ji<j but a[i]>a[j]a[i] > a[j]a[i]>a[j]. Given an array, design a linearithmic algorithm to count the number of inversions.


## Question 3

Shuffling a linked list. Given a singly-linked list containing nnn items, rearrange the items uniformly at random. Your algorithm should consume a logarithmic (or constant) amount of extra memory and run in time proportional to nlog⁡nn \log nnlogn in the worst case. 
