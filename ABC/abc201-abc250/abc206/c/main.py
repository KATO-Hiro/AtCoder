# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = n * (n - 1) // 2

    for ci in c.values():
        ans -= ci * (ci - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
