# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    print(max(c.values()))


if __name__ == '__main__':
    main()
