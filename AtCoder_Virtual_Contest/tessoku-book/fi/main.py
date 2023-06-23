# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    left = 1
    right = 10**9

    def f(x):
        count = 0

        for ai in a:
            count += int(ai / x)

        return count

    for _ in range(100):
        wj = (right + left) / 2

        if f(wj) >= k:
            left = wj
        else:
            right = wj

    ans = [int(ai / left) for ai in a]
    print(*ans)


if __name__ == "__main__":
    main()
