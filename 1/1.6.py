# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string a a b c c c c c a a a would become a 2 b l c 5 a 3 , If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, if 110

string = 'aaaaabbcccccddde'

for letter in list(set(string)):
    count = string.count(letter)
    print(letter, count)
