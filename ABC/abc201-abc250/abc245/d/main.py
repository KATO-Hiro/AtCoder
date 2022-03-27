# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))[::-1]
    c = list(map(int, input().split()))[::-1]
    b = list()

    for i in range(m + 1):
        if a[0] == 0:
            continue

        p, q = divmod(c[i], a[0])

        for j in range(n + 1):
            c[i + j] -= p * a[j]

        b.append(p)

    print(*b[::-1])


if __name__ == "__main__":
    main()
