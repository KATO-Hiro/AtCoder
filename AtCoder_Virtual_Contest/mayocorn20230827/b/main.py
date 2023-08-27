# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    h = sorted([int(input()) for _ in range(n)])
    ans = 10**18

    for i in range(n):
        j = i + k - 1

        if j >= n:
            break

        ans = min(ans, h[j] - h[i])

    print(ans)


if __name__ == "__main__":
    main()
