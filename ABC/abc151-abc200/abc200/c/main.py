# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = [0 for _ in range(n)]

    for index, ai in enumerate(a):
        b[index] = ai % 200

    c = Counter(b)

    ans = 0

    for ci in c.values():
        ans += ci * (ci - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
