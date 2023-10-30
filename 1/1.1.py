# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

strings = ['abcd', 'aaabbb', 'test12345']

def check_unique_values(string):
    return True if len(string) == len(list(set(string))) else False

for string in strings:
    print(string, check_unique_values(string))
