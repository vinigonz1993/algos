# Partition: Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater
# than or equal to x.
# If x is contained within the list, the values of x only need
# to be after the elements less than x (see below).
# The partition element x can appear anywhere in the "right partition";
# it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from linked_list import LinkedList


class CustomLinkedList(LinkedList):

    def partition(self, num):
        print(f'[partition = {5}]')
        pass

        current = self.head
        partitioned = []

        while current.data:
            partitioned.append(current.data)
            if current.next is None:
                break

            current = current.next

        index = partitioned.index(num)
        lower = [i for i in partitioned if i < 5]
        greater = [i for i in partitioned if i >= 5]
        print(lower)
        print(greater)
        print(f'Lookup: {index}')

        return [*lower, *greater]


initial_list = [3, 5, 8, 5, 10, 2, 1]

linked_list = CustomLinkedList()
linked_list.generate_list(initial_list)
linked_list.display()

partitioned_list = linked_list.partition(5)

partitioned_linked_list = CustomLinkedList()
partitioned_linked_list.generate_list(partitioned_list)
partitioned_linked_list.display()
