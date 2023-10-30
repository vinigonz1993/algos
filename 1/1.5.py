# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# p a l e , p i e - > t r u e
# p a l e s , p a l e - > t r u e
# p a l e , b a l e - > t r u e
# p a l e , b a k e - > f a l s e
# Hints: #23, #97, it 130

string_list = [
    ('pale', 'pie', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('pale', 'bake', False)
]

def check_one_away_distance(first, second):
    if abs(len(second) - len(first)) > 1:
        return False

    distance = [
        [
            0 for _ in range(len(second) + 1)
        ] for _ in range(len(first) + 1)
    ]

    for i in range(len(first) + 1):
        for j in range(len(second) + 1):
            if i == 0:
                distance[i][j] = j
            elif j == 0:
                distance[i][j] = i
            elif first[i - 1] == second[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(
                    distance[i][j - 1],
                    distance[i - 1][j],
                    distance[i - 1][j - 1]
                )

    print(distance)
    # print(distance[len(first)][len(second)])

    return distance[len(first)][len(second)] == 1

for strings in string_list:
    print(strings[2], check_one_away_distance(strings[0], strings[1]))
