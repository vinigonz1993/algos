# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.

from linked_list import LinkedList

class CustomLinkedList(LinkedList):

    def get_corrupted_node(self):
        values = []

        current = self.head
        corrupt_node = None

        while current.next:
            if current.data in values:
                corrupt_node = current
                break
            values.append(current.data)
            current = current.next
        return corrupt_node

linked_list = CustomLinkedList()

linked_list.generate_list([1, 2, 3, 4, 5, 6, 7, 8, 6, 9, 0])

linked_list.display()
print()
print(linked_list.get_corrupted_node())
