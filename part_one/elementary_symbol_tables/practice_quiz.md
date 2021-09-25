# Interview Questions: Elementary Symbol Tables


## Question 1
Java autoboxing and equals(). Consider two `double` values `a` and `b` and their corresponding `Double` values `x` and `y`.

* Find values such that a==b is `true` but x.equals(y) is `false`.
* Find values such that a==b is `false` but x.equals(y) is `true`.

skipped since it is java specific problem.

## Question 2
Check if a binary tree is a BST. Given a binary tree where each `Node` contains a key, determine whether it is a binary search tree. 
Use extra space proportional to the height of the tree.

A leetcode problem ([98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)). 

## Question 3
Inorder traversal with constant extra space. Design an algorithm to perform an inorder traversal of a binary search tree using 
only a constant amount of extra space.

The time complexity is always `O(n)`, since the goal is to traverse the entire BST, but constant space complexity? The traversal can be done in two ways.
Either iteration with the help of a stack or recursion using the fuction call stack. Both are dependent on the depth of the tree.


## Question 4
Web tracking. Suppose that you are tracking `n` web sites and `m` users and you want to support the following API:

* User visits a website.
* How many times has a given user visited a given site?

What data structure or data structures would you use?

**Answer**:
A nested hashmap. Something like `{user_id: {web_id: count}}`. Each time a user `x` visits a website `y`, the nested hashmap updates the count (or create a new 
key if the user or website not exist in hashmap).
