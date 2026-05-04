# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    right = 0
    mod = 998244353
    ans = 0

    for left in range(n):
        if left > right:
            right = left

        while right + 1 < n and s[right] != s[right + 1]:
            right += 1

        ans += right - left + 1
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
