# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    i = 0
    j = 0

    while i < n:
        if (j < m) and (b[j] <= a[i]):
            j += 1

        i += 1

    if j == m:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
