# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    d = defaultdict(int)

    for _ in range(n):
        ai, bi, ci = map(int, input().split())
        d[(ai, bi)] = ci

    x = list(map(int, input().split()))
    ans = x[0]

    for xi in x[1:]:
        if (ans, xi) in d:
            ans = d[(ans, xi)]
        elif (xi, ans) in d:
            ans = d[(xi, ans)]
        else:
            ans += xi

    print(ans)


if __name__ == "__main__":
    main()
