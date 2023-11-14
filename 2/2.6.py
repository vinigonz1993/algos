# Palindrome: Implement a function to check if a linked list is a palindrome.

from itertools import permutations
from linked_list import LinkedList


class CustomLinkedList(LinkedList):

    def is_palindrome(self):
        current = self.head

        values = []

        while current.data:
            values.append(current.data)
            if current.next is None:
                break

            current = current.next

        palindromes = [p for p in permutations(values)]
        print()
        print(f'{len(palindromes)} palindromes found')


initial_list = 'Tact Coa'.replace(' ', '').lower()


linked_list = CustomLinkedList()
linked_list.generate_list(initial_list)
linked_list.display()

linked_list.is_palindrome()
