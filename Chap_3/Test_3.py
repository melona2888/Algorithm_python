# init Matrix
# Define Matrix
row, col = map(int, input().split())

matrix = list()
min_num = 0

for _ in range(row):
    matrix_row = list(map(int, input().split()))
    diff_num = min(matrix_row)
    matrix.append(matrix_row)
    if min_num < diff_num:
        min_num = diff_num

print(matrix)
print(min_num)