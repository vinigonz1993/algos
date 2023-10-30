# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: ( 7 - > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912

from linked_list import LinkedList

class CustomLinkedList(LinkedList):

    def get_number(self):

        current = self.head

        nums = []

        while current.data:
            nums.append(str(current.data))

            if current.next is None:
                break

            current = current.next
        nums.reverse()
        return int(''.join(nums))


list1 = [7, 1, 6]
list2 = [5, 9, 2]

ll1 = CustomLinkedList()
ll1.generate_list(list1)

ll2 = CustomLinkedList()
ll2.generate_list(list2)

num_ll1 = ll1.get_number()
num_ll2 = ll2.get_number()

num_sums = [i for i in str(num_ll1 + num_ll2)]
num_sums.reverse()

ll3 = CustomLinkedList()
ll3.generate_list(num_sums)
ll3.display()