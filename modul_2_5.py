def get_matrix(n=2, m=2, value=10):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[-1].append([value])
    return matrix
result = get_matrix()
print(result)