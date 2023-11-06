# Stack Min: How would you design a stack which, in addition to p u s h and pop, has a function m i n
# which returns the minimum eiement? Push, p o p and m i n should ail operate in 0 ( 1 ) time.

from stack import Stack


class CustomStack(Stack):

    def __init__(self):
        self.items = []
        self.min_value = None
        self.max_value = None

    def push(self, item):
        self.items.append(item)

        if self.min_value is None or value <= self.min_value:
            self.min_value = value

        if self.max_value is None or value >= self.max_value:
            self.max_value = value

    def min(self):
        return self.min_value

    def max(self):
        return self.max_value

stack = CustomStack()

values = [1, 2, 3, 4, 5, 6, 7, 0]

for value in values:
    stack.push(value)

print(f'Min: {stack.min()}')
print(f'Max: {stack.max()}')
