# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    s = list(map(int, input().split()))
    c = Counter(s)
    print(len(c.keys()), sum(c.keys()))


if __name__ == "__main__":
    main()
