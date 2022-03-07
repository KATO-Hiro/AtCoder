# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    print(c[100] * c[400] + c[200] * c[300])


if __name__ == "__main__":
    main()
