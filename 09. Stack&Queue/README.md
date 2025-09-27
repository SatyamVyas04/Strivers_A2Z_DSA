# Overview

## 9.1. Learning

Stack: LIFO (Last In First Out) data structure. Operations: push, pop, top/peek, isEmpty.
Queue: FIFO (First In First Out) data structure. Operations: enqueue, dequeue, front/peek, isEmpty.
Deque: Double-ended queue, allows insertion and deletion from both ends.
Common applications: expression evaluation, backtracking, BFS, sliding window problems.

## 9.2. Prefix, Infix, Postfix Notation

- Prefix (Polish Notation): Operator before operands (e.g., +AB).
- Infix: Operator between operands (e.g., A + B).
- Postfix (Reverse Polish Notation): Operator after operands (e.g., AB+).
- Conversion: Use stack to convert between notations, considering operator precedence and parentheses.

## 9.3. Monotonic Stack/Queue

These problems were a great eye-opener for me. I had never thought of using stacks/queues to maintain a sorted order of elements. This technique is very useful in solving problems related to finding the next greater/smaller element, sliding window maximum, and histogram problems.

- Monotonic Stack: Stack that maintains elements in sorted order (increasing or decreasing).
- Monotonic Queue: Queue that maintains elements in sorted order.
- Applications: Next Greater Element, Sliding Window Maximum, Histogram problems.

## 9.4. Implementation

Problems like LRU Cache, LFU Cache and be thought of as a combination of stack/queue with hashing. The idea is to use a doubly linked list to maintain the order of elements and a hash map to store the references to the nodes in the linked list for O(1) access.

## Important Questions

| Topic           | Rating | Question             | Solution Link                                             | Date          |
| :-------------- | :----- | :------------------- | :-------------------------------------------------------- | :------------ |
| Stack and Queue | Easy   | Next Smaller Element | [Here](./9.3.%20Monotonic/1.%20NextGreaterElementLeet.py) | 1st June 2024 |
| Stack and Queue | Medium | Pre Post and Infix   | [Here](./9.2.%20Pre_In_Pro/)                              | 1st June 2024 |
| Stack and Queue | Medium | Asteroid Collision   | [Here](./9.3.%20Monotonic/7.%20AsteroidLeet.py)           | 2nd June 2024 |
| Stack and Queue | Hard   | Trapping Rainwater   | [Here](./9.3.%20Monotonic/5.%20TrappingRainwaterLeet.py)  | 2nd June 2024 |
| Stack and Queue | Hard   | Sum of Subarr        | [Here](./9.3.%20Monotonic/6.%20SumSubarrMinLeet.py)       | 2nd June 2024 |
| Stack and Queue | Hard   | Largest Rectangle    | [Here](./9.3.%20Monotonic/10.%20LargestRectLeet.py)       | 2nd June 2024 |
| Stack and Queue | Hard   | LFU Cache            | [Here](./9.4.%20Implementation/5.%20LFUCache.py)          | 8th June 2024 |

## That's it :)

```plaintext
परित्राणाय साधूनां
विनाशाय च दुष्कृताम् ।
धर्मसंस्थापनार्थाय
संभवामि युगे युगे ॥

4.8
```

> To protect the righteous, to annihilate the wicked, and to re-establish the principles of dharma, I appear millennium after millennium.
