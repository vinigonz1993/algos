# Zero Matrix: Write an algorithm such that if an element in
# an MxN matrix is 0, its entire row and
# column are set to 0.

matrix = [
    [1, 1, 1],
    [1, 0, 0],
    [2, 2, 2]
]


for row in range(0, len(matrix)):
    if matrix[row].count(0) > 0:
        matrix[row] = [0 for _ in range(0, len(matrix[row]))]


print(matrix)
