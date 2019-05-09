# -*- coding: utf-8 -*-


def main():
    from itertools import combinations

    n = int(input())
    xys = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for xy in combinations(xys, 3):
        x0 = xy[0][0]
        y0 = xy[0][1]

        x1 = xy[1][0] - x0
        y1 = xy[1][1] - y0
        x2 = xy[2][0] - x0
        y2 = xy[2][1] - y0
        s = abs(x1 * y2 - x2 * y1)

        if s > 0 and s % 2 == 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
