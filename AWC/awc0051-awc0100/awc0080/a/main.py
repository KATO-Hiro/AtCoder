# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    h = list(map(int, input().split()))

    for _ in range(m):
        tj, dj = map(int, input().split())
        tj -= 1

        h[tj] -= dj

        prev = tj - 1
        next = tj + 1

        if prev >= 0:
            h[prev] -= dj // 2
        if next < n:
            h[next] -= dj // 2

    ans = sum([1 for hi in h if hi >= 1])
    print(ans)


if __name__ == "__main__":
    main()
