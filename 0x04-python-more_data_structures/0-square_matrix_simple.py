#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    result_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

            return result_matrix

# Example usage
input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output_matrix = square_matrix_simple(input_matrix)
print(output_matrix)
