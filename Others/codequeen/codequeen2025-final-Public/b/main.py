# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter()
    ans = 0

    for ai in a:
        ans += c[s - ai]
        c[ai] += 1

    print(ans)


if __name__ == "__main__":
    main()
