# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    # print(s)
    inf = 10**18
    ans = inf
    batsu, dot = "x", "."

    # 横方向
    if w >= k:
        for i in range(h):
            d = defaultdict(int)

            for x in range(k):
                d[s[i][x]] += 1

            if d[batsu] == 0:
                ans = min(ans, d[dot])

            for j in range(k, w):
                d[s[i][j]] += 1
                d[s[i][j - k]] -= 1

                if d[batsu] == 0:
                    ans = min(ans, d[dot])

    # 縦方向
    if h >= k:
        for j in range(w):
            d = defaultdict(int)

            for y in range(k):
                d[s[y][j]] += 1

            if d[batsu] == 0:
                ans = min(ans, d[dot])

            for i in range(k, h):
                d[s[i][j]] += 1
                d[s[i - k][j]] -= 1

                if d[batsu] == 0:
                    ans = min(ans, d[dot])

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
