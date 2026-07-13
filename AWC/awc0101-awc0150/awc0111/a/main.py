# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    ans = 0

    for _ in range(n):
        s = list(map(int, input().split()))

        if m >= 3:
            summed = sum(s) - (max(s) + min(s))
            summed /= m - 2
        else:
            summed = sum(s)
            summed /= m

        if summed < k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
