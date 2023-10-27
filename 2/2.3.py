# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a->b->d->e-> f

from linked_list import LinkedList

class CustomLinkedList(LinkedList):

    def remove_node(self, node):
        if not self.head:
            return

        current = self.head

        while current.next:
            if current.data == node:
                current.next = current.next.next
                return
            current = current.next


initial_list = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9]

linked_list = CustomLinkedList()

for i in initial_list:
    linked_list.append(i)

print(linked_list.display())

linked_list.remove_node(4)

print(linked_list.display())
