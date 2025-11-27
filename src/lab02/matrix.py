print("Вывод на задание transpose:")


def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    row_1len = len(mat[0])
    for row in mat:
        if len(row) != row_1len:
            return "ValueError"
    return [list(pillar) for pillar in zip(*mat)]


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

print("Вывод на задание row_sums:")


def row_sums(mat: list[list[float | int]]) -> list[float]:
    list_length = (len(row) for row in mat)
    if len(set(list_length)) != 1:
        return "ValueError"
    result = 0
    return list(map(int, (sum(x) for x in mat)))


print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print("Вывод на задание col_sums:")


def col_sums(mat: list[list[float | int]]) -> list[float]:
    list_length = (len(row) for row in mat)
    if len(set(list_length)) != 1:
        return "ValueError"
    summa_mat = []
    for j in range(len(mat[0])):
        summa = 0
        for i in range(len(mat)):
            summa += mat[i][j]
        summa_mat.append(summa)
    return summa_mat


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
