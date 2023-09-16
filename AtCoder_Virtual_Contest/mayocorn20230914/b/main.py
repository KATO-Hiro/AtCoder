# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = 0

    for ai, bi in ab:
        count_min = min(bi, m)
        m -= count_min
        ans += count_min * ai

        if m == 0:
            break

    print(ans)


if __name__ == "__main__":
    main()
