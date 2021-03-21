# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    h, w, a, b = map(int, input().split())
    tiles = list()

    for i in range(h):
        for j in range(w - 1):
            tiles.append(((i, j), (i, j + 1)))

    for i in range(h - 1):
        for j in range(w):
            tiles.append(((i, j), (i + 1, j)))

    ans = 0

    for c in combinations(tiles, a):
        board = [[0 for _ in range(w)] for _ in range(h)]

        for first, second in c:
            board[first[0]][first[1]] += 1
            board[second[0]][second[1]] += 1

        max_value = 0

        for i in range(h):
            for j in range(w):
                max_value = max(max_value, board[i][j])

        if max_value > 1:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
