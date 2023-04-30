# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, ci = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(ci)]
    c = [list(map(int, input().split())) for _ in range(n)]

    # 3種類に塗り分ける + 各種類についてどの色で塗られているかまとめる
    color_counts = [[0 for _ in range(30)] for _ in range(3)]

    for i in range(n):
        for j in range(n):
            group_id = (i + j) % 3
            color_id = c[i][j] - 1  # 0-indexed
            color_counts[group_id][color_id] += 1
    
    # c色から3種類選んで、全探索
    ans = float("inf")

    for c1, c2, c3 in permutations(range(ci), 3):
        candidate = 0

        for j in range(ci):
            candidate += d[j][c1] * color_counts[0][j]
            candidate += d[j][c2] * color_counts[1][j]
            candidate += d[j][c3] * color_counts[2][j]

        ans = min(ans, candidate)
    
    print(ans)


if __name__ == "__main__":
    main()
