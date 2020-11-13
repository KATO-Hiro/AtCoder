# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    ans = [[0 for _ in range(m)] for _ in range(n)]

    dxy = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for y in range(n):
        for x in range(m):
            count = 0

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= m:
                    continue
                if ny < 0 or ny >= n:
                    continue

                if s[ny][nx] == "#":
                    count += 1

            ans[y][x] = count

    for a in ans:
        print("".join(map(str, a)))


if __name__ == "__main__":
    main()
