# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w = map(int, input().split())
    n = int(input())
    d = defaultdict(int)
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1), (0, 0)]

    # いちごが置かれているマス + 隣接8マスでカウントが増える
    for _ in range(n):
        ai, bi = map(int, input().split())

        for dx, dy in dxy:
            nx = bi + dx
            ny = ai + dy

            d[(ny, nx)] += 1

    print(max(d.values()))


if __name__ == "__main__":
    main()
