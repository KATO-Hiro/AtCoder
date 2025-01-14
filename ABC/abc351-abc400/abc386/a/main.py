# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    numbers = list(map(int, input().split()))
    c = Counter(numbers)
    values = sorted(c.values())

    if values == [1, 3] or values == [2, 2]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
