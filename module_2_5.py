def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

#n = int(input())
#m = int(input())
#value = input()
matrix1 = get_matrix(3, 3, 15)
matrix2 = get_matrix(6, 4, 8)
matrix3 = get_matrix(5, 3, 16)
print(matrix1)
print(matrix2)
print(matrix3)