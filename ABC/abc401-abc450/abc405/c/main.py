# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    summed = sum(a)
    ans = 0

    for i in range(n - 1):
        summed -= a[i]
        ans += a[i] * summed

    print(ans)


if __name__ == "__main__":
    main()
