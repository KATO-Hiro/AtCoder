# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    f = list(map(int, input().split()))
    c = Counter(f)
    values = c.values()

    if 2 in values and 3 in values:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
