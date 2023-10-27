# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


n = len(matrix)
layers = len(matrix) // 2

for layer in range(layers):
    first = layer
    last = n - 1 - layer

    for i in range(first, last):
        offset = i - first

        # Save the top element
        top = matrix[first][i]

        # Move left to top
        matrix[first][i] = matrix[last - offset][first]

        # Move bottom to left
        matrix[last - offset][first] = matrix[last][last - offset]

        # Move right to bottom
        matrix[last][last - offset] = matrix[i][last]

        # Move top to right
        matrix[i][last] = top

for row in matrix:
    print(row)