# Stack and Queue

## Randomized Queue

I have thought about different implementations of a randomized queue.

### Origianl Array

This solution uses the list in Python. For sample or dequeue, I use the result from random value divide by the length of the list as the sampled index then switch the value at sampled index with the value at the end of the queue and use the pop function.

The problem is that in this implementation the enqueue takes linear time.

### Linked List with Hash Map

The doubly linked list stores the value. Hashmap uses the value in linked list as key and maps to node in linked list. In this way, the enqueue takes only constant time. For sample or dequeue the time complexity is `O(n)`.

### Resizing Array

This solution uses the list in Python. But instead of using an empty array in method 1, I specifically declared the initial elements in the list, like `[None, None, None , ... None]`. When enqueuing, start from the middle of the list. Dequeue and sample methods are the same as them in method 1. After some certain time of enqueue, the font of the list is full. When this situation happens, an resizing function is called. Move the stored values in the queue to a larger list middle. In this way, the enqueue function takes a constant amortized time complexity.
