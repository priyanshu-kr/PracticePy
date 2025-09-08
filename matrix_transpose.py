def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

print(transpose_matrix([[1,2,3], [4,5,6]]))