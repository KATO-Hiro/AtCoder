# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    d = defaultdict(set)

    for i in range(h):
        for j in range(w):
            d[i + j].add(s[i][j])

    mod = 998244353
    ans = 1

    for value in d.values():
        if "R" in value and "B" in value:
            ans *= 0
            break

        if len(value) == 1 and "." in value:
            ans *= 2
            ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
