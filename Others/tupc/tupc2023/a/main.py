# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    xyp = [tuple(map(int, input().split())) for _ in range(n)]
    px, py = defaultdict(int), defaultdict(int)

    for xi, yi, pi in xyp:
        px[xi] += pi
        py[yi] += pi

    ans = 0

    for xi, yi, pi in xyp:
        ans = max(ans, px[xi] + py[yi] - pi)

    print(ans)


if __name__ == "__main__":
    main()
