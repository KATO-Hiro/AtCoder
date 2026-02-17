# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [(ai, i) for i, ai in enumerate(a)]

    while len(a) >= 2:
        b = []
        size = len(a)

        for i in range(0, size, k):
            best, id = -1, -1

            for j in range(i, min(i + k, size)):
                if a[j][0] > best:
                    best, id = a[j]

            b.append((best, id))

        a = b

    print(a[0][1] + 1)


if __name__ == "__main__":
    main()
