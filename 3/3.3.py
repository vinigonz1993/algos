# Stack of Plates: Imagine a (literal) stack of plates.
# If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when
# the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this.
# SetOfStacks should be composed of several stacks and
# should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically
# to a single stack (that is, pop() should return the same values
# as it would if there were just a single stack).

from stack import Stack


class CustomStack(Stack):

    def __init__(self):
        self.items = [[]]
        self.stack_limit = 5

    def push(self, item):
        pointer = 0
        check = True

        while check:
            try:
                if len(self.items[pointer]) < self.stack_limit:
                    check = False
                else:
                    pointer += 1
            except IndexError:
                self.items.append([])
                check = False

        self.items[pointer].append(item)

        print(self.items)


values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 22, 3, 11]

stack = CustomStack()

for value in values:
    stack.push(value)
