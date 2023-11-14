# Sort Stack: Write a program to sort a stack such that the
# smallest items are on the top.
# You can use an additional temporary stack, but you may not
# copy the elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and is Empty.

from stack import Stack


class CustomStack(Stack):

    def sort(self):
        '''
            Generates a temporary stack ordering from
            lowest to greatest. Then, pushes all the sorted
            values to the original stack.
        '''
        tmp_stack = []

        while self.items:
            current_value = self.items.pop()

            while tmp_stack and tmp_stack[-1] > current_value:
                self.items.append(tmp_stack.pop())

            tmp_stack.append(current_value)

        while tmp_stack:
            self.items.append(tmp_stack.pop())

    def display(self):
        print(self.items)


values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

stack = CustomStack()

for value in values:
    stack.push(value)

stack.display()
stack.sort()
stack.display()
