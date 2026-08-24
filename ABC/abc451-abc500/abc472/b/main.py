# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    l = list(map(int, input().split()))
    left, right = 0, sum(l)
    inf = 10**18
    ans = inf

    for i in range(n - 1):
        left += l[i]
        right -= l[i]
        ans = min(ans, abs(right - left))

    print(ans)


if __name__ == "__main__":
    main()
