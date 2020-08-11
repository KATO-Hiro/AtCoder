# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    operations = list()

    # See:
    # https://atcoder.jp/contests/abc109/submissions/3154532
    for row in range(h):
        for col in range(w - 1):
            if a[row][col] % 2 == 1:
                operations.append((row + 1, col + 1, row + 1, col + 2))
                a[row][col] -= 1
                a[row][col + 1] += 1

    for row in range(h - 1):
        if a[row][w - 1] % 2 == 1:
            operations.append((row + 1, w, row + 2, w))
            a[row][w - 1] -= 1
            a[row + 1][w - 1] += 1

    n = len(operations)
    print(n)

    for i in range(n):
        y, x, y_dash, x_dash = operations[i]
        print(y, x, y_dash, x_dash)


if __name__ == '__main__':
    main()
