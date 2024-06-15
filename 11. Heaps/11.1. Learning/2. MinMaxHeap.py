# Leaving the GFG aside, here's the implementation for min and max heap, the normal way
import heapq

# Starter Array
A = [1, 3, 4, 2, 5, 7, 5, 6, 8]

# Convert the list into a max-heap
heapq._heapify_max(A)  # Max Heap
print(A)

# Convert the list back into a min-heap
heapq.heapify(A)  # Min Heap
print(A)

# Push a new element into the heap
heapq.heappush(A, -1)  # Push in
print(A)

# Pop the smallest element from the heap
print(heapq.heappop(A))  # Pop out
print(A)

# Push a new element and then pop the smallest element from the heap
print(heapq.heappushpop(A, -1))  # Push then Pop Together
print(A)

# Pop the smallest element and then push a new element into the heap
print(heapq.heapreplace(A, -1))  # Pop then Push Together
print(A)
