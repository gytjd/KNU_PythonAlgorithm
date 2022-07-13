import sys

row, col = map(int, sys.stdin.readline().split())

array = []
result = []

for _ in range(row):
    pic = input()
    array.append(pic)


def count_pic(a, b):
    count = 0
    for i in range(a, 8 + a):
        if array[a][b] == 'B':
            if i % 2 == a:
                for j in range(b, 8 + b, +2):
                    if array[i][j] != 'B':
                        count += 1

                for j in range(b + 1, 8 + b, +2):
                    if array[i][j] != 'W':
                        count += 1
            else:
                for j in range(b, 8 + b, +2):
                    if array[i][j] != 'W':
                        count += 1
                for j in range(b + 1, 8 + b, +2):

                    if array[i][j] != 'B':
                        count += 1

        else:
            if i % 2 == a:
                for j in range(b, 8 + b, +2):
                    if array[i][j] != 'W':
                        count += 1

                for j in range(b + 1, 8 + b, +2):
                    if array[i][j] != 'B':
                        count += 1

            else:
                for j in range(b, 8 + b, +2):
                    if array[i][j] != 'B':
                        count += 1
                for j in range(b + 1, 8 + b, +2):
                    if array[i][j] != 'W':
                        count += 1

    return count


def count_pic_1(a, b):
    count = 0
    for i in range(a, 8 + a):
        if array[a][b] == 'B':
            if i % 2 == a:
                for j in range(b, 8 + b, +2):
                    if array[i][j] != 'W':
                        count += 1

                for j in range(b + 1, 8 + b, +2):
                    if array[i][j] != 'B':
                        count += 1
            else:
                for j in range(b, 8 + b, +2):
                    if array[i][j] != 'B':
                        count += 1
                for j in range(b + 1, 8 + b, +2):

                    if array[i][j] != 'W':
                        count += 1

        else:
            if i % 2 == a:
                for j in range(b, 8 + b, +2):
                    if array[i][j] != 'B':
                        count += 1

                for j in range(b + 1, 8 + b, +2):
                    if array[i][j] != 'W':
                        count += 1

            else:
                for j in range(b, 8 + b, +2):
                    if array[i][j] != 'W':
                        count += 1
                for j in range(b + 1, 8 + b, +2):
                    if array[i][j] != 'B':
                        count += 1

    return count


for i in range(row - 8 + 1):
    for j in range(col - 8 + 1):
        result.append(count_pic(i, j))
        result.append(count_pic_1(i, j))

print(min(result))
