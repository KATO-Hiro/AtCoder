# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    operations = list()
    row = 0
    prev_x, prev_y = 0, 0
    odd_count = 0

    while row < h:
        if row % 2 == 0:
            for col in range(w):
                if a[row][col] % 2 == 1:
                    if odd_count == 0:
                        prev_x, prev_y = col + 1, row + 1
                        odd_count = 1
                    else:
                        cur_x, cur_y = col + 1, row + 1
                        operations.append((prev_y, prev_x, cur_y, cur_x))
                        prev_x, prev_y = cur_x, cur_y
                        odd_count = 0
                else:
                    if odd_count == 1:
                        cur_x, cur_y = col + 1, row + 1
                        operations.append((prev_y, prev_x, cur_y, cur_x))
                        prev_x, prev_y = cur_x, cur_y
        else:
            for col in range(w - 1, -1, -1):
                if a[row][col] % 2 == 1:
                    if odd_count == 0:
                        prev_x, prev_y = col + 1, row + 1
                        odd_count = 1
                    else:
                        cur_x, cur_y = col + 1, row + 1
                        operations.append((prev_y, prev_x, cur_y, cur_x))
                        prev_x, prev_y = cur_x, cur_y
                        odd_count = 0
                else:
                    if odd_count == 1:
                        cur_x, cur_y = col + 1, row + 1
                        operations.append((prev_y, prev_x, cur_y, cur_x))
                        prev_x, prev_y = cur_x, cur_y

        row += 1

    n = len(operations)
    print(n)

    for i in range(n):
        y, x, y_dash, x_dash = operations[i]
        print(y, x, y_dash, x_dash)


if __name__ == '__main__':
    main()
