# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [["" for _ in range(n)] for _ in range(n)]
    used = [[False for _ in range(n)] for _ in range(n)]
    m = n // 2
    s[m][m] = "T"
    used[m][m] = True
    # print(s)
    i, j, dir = 0, 0, 0
    dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dy, dx = dyx[dir]
    value = 1

    while s[i][j] != "T":
        s[i][j] = str(value)
        value += 1
        used[i][j] = True

        i += dy
        j += dx

        if i == -1 or i == n or j == -1 or j == n or used[i][j]:
            # rollback
            i -= dy
            j -= dx

            dir = (dir + 1) % 4
            dy, dx = dyx[dir]
            i += dy
            j += dx

    # print(s)

    for si in s:
        print(*si)


if __name__ == "__main__":
    main()
