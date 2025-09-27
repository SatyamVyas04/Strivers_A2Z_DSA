# Overview

## 6.1. Linked List Introduction

- What is a Linked List?
  A linked list is a linear data structure where elements, called nodes, are stored in a sequence. Each node contains data and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory allocation, allowing for dynamic memory usage and efficient insertions and deletions.

- Types of Linked Lists:
  - Singly Linked List: Each node points to the next node in the sequence.
  - Doubly Linked List: Each node contains pointers to both the next and previous nodes, allowing for bidirectional traversal.
  - Circular Linked List: The last node points back to the first node, forming a circular structure. This can be implemented in both singly and doubly linked lists.

- Basic Operations:
  - Insertion: Adding a new node to the list (at the beginning, end, or a specific position).
  - Deletion: Removing a node from the list.
  - Traversal: Accessing each node in the list sequentially.
  - Searching: Finding a node with a specific value.
  - Updating: Modifying the value of a node.

- Advantages of Linked Lists:
  - Dynamic Size: Linked lists can grow and shrink in size as needed, unlike arrays
  - Efficient Insertions/Deletions: Adding or removing nodes is generally more efficient than in arrays, especially for large datasets.
  - Memory Utilization: Linked lists can utilize memory more efficiently by allocating memory as needed.

- Disadvantages of Linked Lists:
  - Memory Overhead: Each node requires additional memory for storing pointers, which can lead
    to increased memory usage compared to arrays.
  - Sequential Access: Linked lists do not support random access, making certain operations slower compared to arrays.
  - Complexity: Implementing and managing linked lists can be more complex than arrays, especially for beginners.

## 6.2. Doubly Linked List

A doubly linked list is a type of linked list where each node contains three fields: a data field, a pointer to the next node, and a pointer to the previous node. This allows for traversal in both directions (forward and backward).

## 6.3. Medium Level Problems

This section was literally eye-opening. I never thought of using a dummy node to simplify edge cases in linked list problems. This technique can make the code cleaner and easier to understand by avoiding special cases for head and tail nodes. Learnt a lot like reversing a linked list, finding the middle node, detecting cycles, and merging two sorted linked lists. These problems helped me understand the importance of pointers and how to manipulate them effectively.

## 6.4. Medium Level Doubly Linked List Problems

Similar to the section above, just with doubly linked lists. The added complexity of having both next and previous pointers made me think more about how to maintain the integrity of the list during operations like insertion and deletion.

## 6.5. Hard Level Problems

Problems like rotating a linked list, and cloning it. These problems required a deeper understanding of linked list structures.

## Important Questions

| Topic      | Rating | Question                            | Solution Link                                     | Date          |
| :--------- | :----- | :---------------------------------- | :------------------------------------------------ | :------------ |
| LinkedList | Medium | Check for all cases during Deletion | [Here](./6.2.%20DLL/3.%20DeleteLastNode.py)       | 10th Jan 2024 |
| LinkedList | Medium | Cycle Detection Standard            | [Here](./6.3.%20MediumLL/4.%20CycleDetection.py)  | 10th Jan 2024 |
| LinkedList | Medium | Cycle Start Detection               | [Here](./6.3.%20MediumLL/5.%20StartOfCycle.py)    | 10th Jan 2024 |
| LinkedList | Medium | Cycle Length Detection              | [Here](./6.3.%20MediumLL/6.%20LengthOfCycle.py)   | 10th Jan 2024 |
| LinkedList | Medium | Addition of Numbers                 | [Here](./6.3.%20MediumLL/15.%20AddNumbersLeet.py) | 11th Jan 2024 |
| LinkedList | Hard   | Clone of given LL                   | [Here](./6.5.%20HardLL/4.%20Clone.py)             | 12th Jan 2024 |

## That's it :)

```plaintext
योगस्थः कुरु कर्माणि
सङ्गं त्यक्त्वा धनञ्जय ।
सिद्ध्यसिद्ध्योः समो भूत्वा
समत्वं योग उच्यते ॥

2.48
```

> Perform your duty, O Arjuna, abandoning attachment, and be balanced in success and failure. This equanimity is called Yoga.
