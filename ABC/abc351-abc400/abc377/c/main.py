# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = set()
    dxy = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        s.add((ai, bi))

        for dx, dy in dxy:
            ny = ai + dy
            nx = bi + dx

            if ny <= 0 or nx <= 0 or ny > n or nx > n:
                continue
            if (ny, nx) in s:
                continue

            s.add((ny, nx))

    ans = n**2 - len(s)
    print(ans)


if __name__ == "__main__":
    main()
