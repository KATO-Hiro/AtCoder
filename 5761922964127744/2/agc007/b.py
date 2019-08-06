# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = list(map(int, input().split()))
    a = [2 * x - 1 for x in range(1, n + 1)]
    b = [-x + (n + 1) for x in range(1, n + 1)]
    sorted_a = [0 for _ in range(n)]
    sorted_b = [0 for _ in range(n)]

    for index, pi in enumerate(p):
        sorted_a[index] = a[pi - 1]
        sorted_b[index] = b[pi - 1]

    print(' '.join(map(str, sorted_a)))
    print(' '.join(map(str, sorted_b)))


if __name__ == '__main__':
    main()
