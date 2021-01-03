# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, large_c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(large_c)]
    c = [list(map(int, input().split())) for _ in range(n)]
    count = [[0 for _ in range(large_c)] for _ in range(3)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count[((i + j) % 3) - 1][c[i - 1][j - 1] - 1] += 1

    patterns = permutations(range(large_c), 3)
    ans = float("inf")

    for pattern in patterns:
        cost = 0

        for index, new_c in enumerate(pattern):
            for old_c in range(large_c):
                cost += d[old_c][new_c] * count[index][old_c]

        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()
