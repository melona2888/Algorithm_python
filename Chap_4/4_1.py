# Input Data
matrix_num = int(input())
routine = list(map(str, input().split()))

# Init Value
cord = [1, 1]

# Going

for _ in range(len(routine)):
    # print(routine.pop(0))
    val = routine.pop(0)
    if val == 'L':
        if cord[1] == 1:
            continue
        cord[1] -= 1

    elif val == 'R':
        if cord[1] >= matrix_num:
            continue
        cord[1] += 1

    elif val == 'U':
        if cord[0] == 1:
            continue
        cord[0] -= 1

    elif val == 'D':
        if cord[0] >= matrix_num:
            continue
        cord[0] += 1


# print(matrix_num)
# print(routine)
print(cord)