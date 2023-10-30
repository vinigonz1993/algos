# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

string1 = 'abcdef'
string2 = 'fedcba'
string3 = '123456'

def check_permutation(first, second):
    return True if set(first) == set(second) else False

print(string1, string2, check_permutation(string1, string2))
print(string2, string3, check_permutation(string2, string3))
print(string3, string1, check_permutation(string3, string1))