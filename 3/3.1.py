# Three in One: Describe how you could use a single array to implement three stacks.
# Hints: #2, #12, #38, #58

from stack import Stack

class StackFromList(Stack):

    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [None] * (3 * stack_size)
        self.stack_pointers = [0, stack_size, 2 * stack_size]
        print(f'Initial array: {self.array}')
        print(f'Pointers: {self.stack_pointers}')

    def push(self, stack_num, value):
        if not self.is_full(stack_num):
            top_index = self.get_top_index(stack_num)
            self.array[top_index] = value
            self.stack_pointers[stack_num] += 1
        else:
            print(f"Stack {stack_num} is full. Cannot push {value}.")

    def pop(self, stack_num):
        if not self.is_empty(stack_num):
            top_index = self.get_top_index(stack_num)
            value = self.array[top_index - 1]
            self.array[top_index - 1] = None
            self.stack_pointers[stack_num] -= 1
            return value
        else:
            print(f"Stack {stack_num} is empty. Cannot pop.")

    def peek(self, stack_num):
        top_index = self.get_top_index(stack_num)
        return self.array[top_index - 1] if top_index > 0 else None

    def is_empty(self, stack_num):
        return self.stack_pointers[stack_num] == stack_num * self.stack_size

    def is_full(self, stack_num):
        return self.stack_pointers[stack_num] == (stack_num + 1) * self.stack_size

    def get_top_index(self, stack_num):
        return self.stack_pointers[stack_num]

stacks = StackFromList(5)

stacks.push(0, 1)
stacks.push(0, 2)
stacks.push(1, 11)
stacks.push(2, 21)
stacks.push(2, 22)

print(stacks.pop(0))
print(stacks.pop(1))
print(stacks.pop(2))
