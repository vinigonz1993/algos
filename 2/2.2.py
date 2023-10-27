# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked lis

from linked_list import LinkedList

class CustomLinkedList(LinkedList):

    def find_position(self, n):
        if not self.head:
            return

        current = self.head

        index = 0

        while index < n:
            if index < n:
                index += 1
                current = current.next
            else:
                print('found')
                print(current.next, current.next.next)
                current.next = current.next.next

        return f'Pos #{n} is {current.data}'

initial_list = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9]

linked_list = CustomLinkedList()

for i in initial_list:
    linked_list.append(i)

print(linked_list.display())
print(linked_list.find_position(5))