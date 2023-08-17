# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    a = [i for i in range(1, 2 * n + 1)]

    for _ in range(m):
        k = int(input())
        b = [0] * (2 * n)

        if k == 0:
            first, second = a[:n], a[n:]

            for i, (f, s) in enumerate(zip(first, second)):
                b[2 * i] = f
                b[2 * i + 1] = s
        else:
            for i in range(2 * n):
                if i < k:
                    b[2 * n - k + i] = a[i]
                else:
                    b[i - k] = a[i]

        a = b

    print(*a, sep="\n")


if __name__ == "__main__":
    main()
