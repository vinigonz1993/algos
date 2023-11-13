# Queue via Stacks: Implement a MyQueue class which implements a
# queue using two stacks.

class MyQueue:
    def __init__(self):
        self.queue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.queue_stack.append(item)

    def dequeue(self):
        '''
            Checks if the dequeue stack is empty. If
            it is empyt, move the top element from the queue
            to the dequeue list. Do that untill dequeue is empty
        '''
        if not self.dequeue_stack:
            while self.queue_stack:
                self.dequeue_stack.append(self.queue_stack.pop())

        if not self.dequeue_stack:
            return None

        return self.dequeue_stack.pop()

    def is_empty(self):
        return not self.queue_stack and not self.dequeue_stack

    def size(self):
        return len(self.queue_stack) + len(self.dequeue_stack)

    def display(self):
        print(f"Queue: {self.queue_stack}")
        print(f"Dequeue: {self.dequeue_stack}")

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()
print()
queue.dequeue()
queue.display()
print()
queue.dequeue()
queue.display()
print()
queue.dequeue()
queue.display()
print()
queue.dequeue()
queue.display()