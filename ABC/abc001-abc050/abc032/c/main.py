# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = [int(input()) for _ in range(n)]

    if 0 in s:
        print(n)
        exit()

    left = 0
    value = 1
    ans = 0

    for right in range(n):
        value *= s[right]

        while (left <= right) and (value > k):
            value //= s[left]
            left += 1

        if value <= k:
            ans = max(ans, right - left + 1)

    print(ans)


if __name__ == "__main__":
    main()
