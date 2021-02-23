# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10 ** 7)
    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    memo = [[None for __ in range(w)] for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    mod = 10 ** 9 + 7

    def dfs(y, x):
        if memo[y][x]:
            return memo[y][x]

        count = 1

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if (nx < 0) or (nx >= w):
                continue
            if (ny < 0) or (ny >= h):
                continue
            if a[ny][nx] < a[y][x]:
                count += dfs(ny, nx)

        memo[y][x] = count % mod

        return count

    ans = 0

    for y in range(h):
        for x in range(w):
            ans += dfs(y, x)
            ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
