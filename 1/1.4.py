# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: T a c t Coa
# Output: T r u e ( p e r m u t a t i o n s : " t a c o c a t " , " a t c o e t a " , e t c . )
# Hints: #106, h 0134, § 136

from itertools import permutations

input = 'Tact Coa'.replace(' ', '').lower()

permutation_list = []
for i in list(permutations(list(input))):
    output = ''.join(i).lower()

    if output == output[::-1]:
        output = f'{output[:4]} {output[4:]}'
        permutation_list.append(output)

print(f'(permutations: {",".join(permutation_list)})')
