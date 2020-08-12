# -*- coding: utf-8 -*-


def main():
    n, m, a, b = map(int, input().split())
    is_a = [0 for _ in range(n)]

    for i in range(m):
        left, right = map(int, input().split())

        for k in range(left - 1, right):
            is_a[k] = 1

    count_a = 0

    for x in is_a:
        if x == 1:
            count_a += 1

    print(count_a * a + (n - count_a) * b)


if __name__ == '__main__':
    main()
