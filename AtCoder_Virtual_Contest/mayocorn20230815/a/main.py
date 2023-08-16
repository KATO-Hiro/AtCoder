# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    c = Counter(a)

    for key, value in c.items():
        if value == 1:
            print(key)
            exit()


if __name__ == "__main__":
    main()
