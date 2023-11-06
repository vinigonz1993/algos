# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure S e t O f S t a c k s that mimics this. S e t O f S t a c k s should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# S e t O f S t a c k s . p u s h ( ) and S e t O f S t a c k s . p o p ( ) should behave identically to a single stack
# (that is, p o p ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function p o p A t ( i n t i n d e x ) which performsa pop operation on a specific sub-stack.

from stack import Stack

class CustomStack(Stack):

    def __init__(self):
        self.items = [[]]
        self.stack_limit = 5

    def push(self, item):
        pointer = 0

values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 22, 3, 11]

stack = CustomStack()

for value in values:
    stack.push(value)


# TODO
# implement the push() method. Verify items and the pointer