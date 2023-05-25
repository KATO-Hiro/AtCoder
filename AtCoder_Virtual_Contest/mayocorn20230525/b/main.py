# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter, defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = defaultdict(int)
    e = Counter((a))

    for ci in c:
        d[b[ci - 1]] += 1

    ans = 0

    for key, value in e.items():
        ans += value * d[key]

    print(ans)


if __name__ == "__main__":
    main()
