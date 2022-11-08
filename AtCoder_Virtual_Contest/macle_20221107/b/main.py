# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    k = int(input())
    a = [0] * n

    # 区間の右端が単調増加 = 尺取り法
    for i, si in enumerate(s):
        if si == '.':
            a[i] = 1

    right, summed = 0, 0
    ans = 0
    
    for left in range(n):
        while right < n and summed + a[right] <= k:
            summed += a[right]
            right += 1
        
        ans = max(ans, right - left)
    
        summed -= a[left]

    print(ans)


if __name__ == "__main__":
    main()
