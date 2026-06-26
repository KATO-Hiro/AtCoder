# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter, defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    d = defaultdict(int)
    count = 0

    for key in sorted(c.keys(), reverse=True):
        value = c[key]
        d[key] = count
        count += value

    ans = []

    for ai in a:
        ans.append(d[ai])

    print(*ans)


if __name__ == "__main__":
    main()
