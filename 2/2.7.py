# Intersection; Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
# secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the j t h node of the second
# linked list, then they are intersecting.

from linked_list import LinkedList, Node

class CustomLinkedList(LinkedList):

    def length(self):
        current = self.head

        total = 0
        while current.next:
            total +=1
            current = current.next

        return total

    def get_node_by_index(self, index):
        current = self.head
        index_count = 0

        while index != index_count:
            index_count += 1
            current = current.next

        return current

    def get_intersection(self, linked_list: Node):
        current = self.head
        currentB = linked_list.head

        current_list_size = self.length()
        linked_list_size = linked_list.length()

        pointer = 0

        if current_list_size != linked_list_size:
            if current_list_size > linked_list_size:
                pointer = current_list_size - linked_list_size - 1
                current = self.get_node_by_index(pointer)
            elif current_list_size < linked_list_size:
                pointer = linked_list_size - current_list_size  - 1
                currentB = self.get_node_by_index(pointer)

        while current != currentB:
            current = current.next
            currentB = currentB.next

            if current.next is None or currentB.next is None:
                return None

        intersection = (current, current.data, current.next)
        print(intersection)
        return intersection

listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]

linked_listA = CustomLinkedList()
linked_listB = CustomLinkedList()
linked_listA.generate_list(listA)
linked_listB.generate_list(listB)

linked_listA.get_intersection(linked_listB)