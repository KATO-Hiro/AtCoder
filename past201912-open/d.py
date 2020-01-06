# -*- coding: utf-8 -*-


def main():
    n = int(input())
    b = [0 for _ in range(n)]

    for i in range(n):
        ai = int(input())
        ai -= 1
        b[ai] += 1

    y = 0
    x = 0

    for index, bi in enumerate(b, 1):
        if bi == 0:
            x = index
        elif bi == 2:
            y = index

    if x == 0 and y == 0:
        print('Correct')
    else:
        print(y, x)


if __name__ == '__main__':
    main()
