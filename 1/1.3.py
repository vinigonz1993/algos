# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: " M r 3ohn S m i t h 13
# Output: " M r % 2 0 3 o h n % 2 0 S m i t h

input = "Mr 3ohn Smith 13"

output = input.replace(' ', '%20')

assert output == "Mr%203ohn%20Smith%2013"

print(output)