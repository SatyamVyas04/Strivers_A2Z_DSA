class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.size = 100001
        self.arr = [0] * self.size

    # Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        # Check if the queue is full
        if (self.rear + 1) % self.size == self.front:
            return
        self.arr[self.rear] = e
        self.rear = (self.rear + 1) % self.size

    # Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        if self.front == self.rear:
            return -1
        popped_item = self.arr[self.front]
        self.front = (self.front + 1) % self.size
        return popped_item
