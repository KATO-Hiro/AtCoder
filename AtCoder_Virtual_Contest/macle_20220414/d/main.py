# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, large_c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(large_c)]
    c = [list(map(int, input().split())) for _ in range(n)]

    before = [defaultdict(int) for _ in range(3)]

    # 前計算: mod 3を取り、各色を集計
    for i in range(n):
        for j in range(n):
            color = c[i][j] - 1
            q = (i + j) % 3

            before[q][color] += 1
    
    # 3色の並びを全探索
    patterns = permutations(range(large_c),3)
    ans = float("inf")

    for after in patterns:
        candidate = 0

        for i, a in enumerate(after):
            for color, count in before[i].items():
                candidate += count * d[color][a]

        ans = min(ans, candidate)
    
    print(ans)


if __name__ == "__main__":
    main()
