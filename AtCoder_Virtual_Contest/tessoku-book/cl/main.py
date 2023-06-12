# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 尺取り法
    left = 0
    summed = 0
    ans = 0

    for right in range(n):
        summed += a[right]

        while left < n and summed > k:
            summed -= a[left]
            left += 1

        ans += right - left + 1

    print(ans)


if __name__ == "__main__":
    main()
