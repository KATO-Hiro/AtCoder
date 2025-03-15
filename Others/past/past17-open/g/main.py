# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    from collections import defaultdict

    input = sys.stdin.readline

    h, w = map(int, input().split())
    d = defaultdict(list)

    for i in range(h):
        gi = input().rstrip()

        for j, gij in enumerate(gi):
            d[gij].append((i, j))

    n = int(input())
    s = input().rstrip()
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

    def dfs(y, x, pos):
        used.add((y, x))

        if pos == n - 1:
            print("Yes")
            exit()

        alpha = s[pos + 1]

        for dx, dy in dxy:
            ny, nx = y + dy, x + dx

            if (ny, nx) not in d[alpha]:
                continue
            if (ny, nx) in used:
                continue

            dfs(ny, nx, pos + 1)

        used.discard((y, x))

    for y, x in d[s[0]]:
        used = set()
        dfs(y, x, 0)

    print("No")


if __name__ == "__main__":
    main()
