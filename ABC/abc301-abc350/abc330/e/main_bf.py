# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(q):
        i, xi = map(int, input().split())
        i -= 1

        a[i] = xi
        b = set(a[:])

        for j in range(n + 1):
            if j not in b:
                print(j)
                break


if __name__ == "__main__":
    main()
