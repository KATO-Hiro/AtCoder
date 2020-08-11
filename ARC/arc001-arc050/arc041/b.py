# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    b = [list(map(int, input())) for _ in range(n)]
    dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    ans = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            value_min = float('inf')

            for dx, dy in dxy:
                nx = j + dx
                ny = i + dy

                value_min = min(value_min, b[ny][nx])

            for dx, dy in dxy:
                nx = j + dx
                ny = i + dy

                b[ny][nx] -= value_min

                ans[i][j] = value_min

    for a in ans:
        print(''.join(map(str, a)))


if __name__ == '__main__':
    main()
