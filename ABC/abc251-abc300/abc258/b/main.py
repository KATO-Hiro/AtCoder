# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(input().rstrip()) * 3 for _ in range(n)]
    b = list()

    for i in range(3 * n):
        j = i % n

        b.append(a[j])

    dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    ans = 0
    hoge = list()

    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            for dx, dy in dxy:
                candidate = b[i][j]
                cur_x, cur_y = j, i

                for m in range(n - 1):
                    nx = cur_x + dx
                    ny = cur_y + dy

                    candidate += b[ny][nx]
                    cur_x = nx
                    cur_y = ny
                
                # hoge.append((candidate, i, j, dx, dy))

                ans = max(ans, int(candidate))

    print(ans)
    # print(sorted(hoge, reverse=True))


if __name__ == "__main__":
    main()
