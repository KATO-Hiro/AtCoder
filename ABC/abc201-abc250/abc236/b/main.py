# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)

    for key, value in c.items():
        if value == 3:
            print(key)
            exit()


if __name__ == "__main__":
    main()
