# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter
    from itertools import combinations

    input = sys.stdin.readline

    a = list(map(int, input().split()))

    for pattern in combinations(a, 5):
        c = Counter(pattern)
        values = list(c.values())

        if values == [2, 3] or values == [3, 2]:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
