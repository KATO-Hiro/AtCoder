# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    right = 1
    ans = n

    for left in range(n - 1):
        d = a[left + 1] - a[left]

        while right < n and a[right] - a[right - 1] == d:
            right += 1

        ans += right - left - 1

    print(ans)


if __name__ == "__main__":
    main()
