# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h, w = n, n
    # h rows * w columns.
    # values: '.' or '#'
    grids = [list(input().rstrip()) for _ in range(h)]
    rows = [0] * n
    cols = [0] * n

    for i in range(n):
        si = grids[i]

        for j, sij in enumerate(si):
            if sij == "o":
                rows[i] += 1
                cols[j] += 1

    ans = 0

    for i in range(n):
        for j in range(n):
            if grids[i][j] == "o":
                ans += (rows[i] - 1) * (cols[j] - 1)

    print(ans)


if __name__ == "__main__":
    main()
