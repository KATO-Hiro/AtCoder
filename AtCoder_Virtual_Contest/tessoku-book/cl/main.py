# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 尺取り法
    right = 0
    summed = 0
    ans = 0

    for left in range(n):
        while right < n and summed + a[right] <= k:
            summed += a[right]
            right += 1

        ans += right - left
        summed -= a[left]

    print(ans)


if __name__ == "__main__":
    main()
