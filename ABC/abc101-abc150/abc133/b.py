# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            total = 0

            for k in range(d):
                total += (x[i][k] - x[j][k]) ** 2

            if total == int(sqrt(total)) ** 2:
                count += 1

    print(count)


if __name__ == '__main__':
    main()
