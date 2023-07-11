# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = n

    for x in sorted(c.keys()):
        count = min(c[x], c[x + 1], c[x + 2])
        c[x] -= count
        c[x + 1] -= count
        c[x + 2] -= count
        ans -= count * 3

    print(ans)


if __name__ == "__main__":
    main()
