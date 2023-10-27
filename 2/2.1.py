# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from linked_list import LinkedList

class CustomLinkedList(LinkedList):

    def remove_duplicates(self):
        if not self.head:
            return

        unique = set()
        current = self.head
        unique.add(current.data)

        while current.next:
            if current.next.data not in unique:
                unique.add(current.next.data)
                current = current.next
            else:
                current.next = current.next.next

initial_list = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9]

linked_list = CustomLinkedList()

for i in initial_list:
    linked_list.append(i)

linked_list.display()

linked_list.remove_duplicates()
linked_list.display()
