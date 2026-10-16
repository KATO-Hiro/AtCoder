# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    d = defaultdict(int)

    for _ in range(n):
        bi, di = map(int, input().split())
        d[bi] = max(d[bi], di)

    ans = sum(d.values())
    print(ans)


if __name__ == "__main__":
    main()
