# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for xy1, xy2 in zip(xy, xy[1:]):
        ans += abs(xy1[0] - xy2[0])
        ans += abs(xy1[1] - xy2[1])

    print(ans)


if __name__ == "__main__":
    main()
