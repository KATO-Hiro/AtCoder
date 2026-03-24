# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)

    for i in range(n - 1):
        ci = list(map(int, input().split()))

        for j, cij in enumerate(ci, i + 1):
            d[(i, j)] = cij
            d[(j, i)] = cij

    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if (d[(a, b)] + d[(b, c)]) < d[(a, c)]:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
