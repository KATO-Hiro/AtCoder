# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = defaultdict(list)

    for _ in range(n):
        ai, bi = map(int, input().split())
        d[ai].append(bi)

    for i in range(1, m + 1):
        di = d[i]
        ans = sum(di) / len(di)
        print(ans)


if __name__ == "__main__":
    main()
