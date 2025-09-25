# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    d = defaultdict(list)
    ans = list()

    for _ in range(k):
        ai, bi = map(int, input().split())
        d[ai].append(bi)

        if len(d[ai]) == m:
            ans.append(ai)

    print(*ans)


if __name__ == "__main__":
    main()
