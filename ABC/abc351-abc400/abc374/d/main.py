# -*- coding: utf-8 -*-


def time(x1, y1, x2, y2, velocity):
    from math import sqrt

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / velocity


def main():
    import sys
    from itertools import permutations, product

    input = sys.stdin.readline

    n, s, t = map(int, input().split())
    abcd = [tuple(map(int, input().split())) for _ in range(n)]
    inf = 10**9
    ans = inf

    # 線分の順番
    for pattern in permutations(range(n)):
        # 線分の向き
        for dir in product([0, 1], repeat=n):
            prev_x, prev_y = 0, 0
            candidate = 0

            for pi, d in zip(pattern, dir):
                ai, bi, ci, di = abcd[pi]

                if d == 1:
                    ai, bi, ci, di = ci, di, ai, bi

                cur_x, cur_y = ai, bi
                candidate += time(prev_x, prev_y, cur_x, cur_y, s)
                candidate += time(ai, bi, ci, di, t)
                prev_x, prev_y = ci, di

            ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
