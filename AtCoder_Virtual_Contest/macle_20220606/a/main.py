# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    b = Counter(a)

    for i in range(1, n + 1):
        total = k - q + b[i]

        if total <= 0:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
