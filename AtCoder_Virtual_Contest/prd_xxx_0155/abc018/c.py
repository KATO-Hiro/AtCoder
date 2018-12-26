# -*- coding: utf-8 -*-


def main():
    r, c, k = map(int, input().split())
    s = [list(input()) for _ in range(r)]
    up = [[0 for __ in range(c)] for _ in range(r)]
    down = [[0 for __ in range(c)] for _ in range(r)]

    # See:
    # https://atcoder.jp/contests/abc018/submissions/3549133
    for j in range(c):
        for i in range(r):
            if s[i][j] == 'o':
                up[i][j] = 1
                down[i][j] = 1

    for j in range(c):
        for i in range(1, r):
            if s[i][j] == 'o':
                up[i][j] = up[i - 1][j] + 1

    for j in range(c):
        for i in range(r - 2, -1, -1):
            if s[i][j] == 'o':
                down[i][j] = down[i + 1][j] + 1

    # See:
    # https://www.slideshare.net/chokudai/abc018
    xy = [(x, y) for y in range(k - 1, c - k + 1) for x in range(k - 1, r - k + 1)]
    ans = 0

    for x, y in xy:
        count = 0

        for z in range(-(k - 1), (k - 1) + 1):
            at_least = k - abs(z)

            if down[x][y + z] >= at_least and up[x][y + z] >= at_least:
                count += 1

        if count == 2 * k - 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
