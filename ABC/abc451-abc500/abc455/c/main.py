# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for ai in a:
        d[ai] += ai

    values = sorted(d.values(), reverse=True)
    size = min(m, len(values))
    ans = sum(a) - sum(values[:size])
    print(ans)


if __name__ == "__main__":
    main()
