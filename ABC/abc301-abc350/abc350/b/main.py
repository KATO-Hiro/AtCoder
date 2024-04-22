# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, q = map(int, input().split())
    t = list(map(int, input().split()))
    c = Counter(t)

    for count in c.values():
        if count % 2 == 1:
            n -= 1

    print(n)


if __name__ == "__main__":
    main()
