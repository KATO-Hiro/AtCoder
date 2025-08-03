# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter()
    ans = 0

    for i, ai in enumerate(a, 1):
        ans += c[i - ai]
        c[i + ai] += 1

    print(ans)


if __name__ == "__main__":
    main()
