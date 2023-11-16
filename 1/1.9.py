# String Rotation; Assume you have a method isSubs t rin g which
# checks if one word is a substring of another.
# Given two strings, si and s2, write code to check if s2 is a
# rotation of si using only one call to isSubs t rin g
# [e.g., "wate r bottle " is a rotation oP'erbottlewat"),


def isSubstring(s1, s2):
    return s2 in s1


def isRotation(s1, s2):
    return len(s1) == len(s2) and isSubstring(s1 + s1, s2)


s1 = "waterbottle"
s2 = "erbottlewat"

print(isSubstring(s1, s2))
print(isRotation(s1, s2))
