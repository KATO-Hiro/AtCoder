# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    to_right = [0] * n
    to_right[0] = a[0]
    to_left = [0] * n
    to_left[-1] = a[-1]

    for i in range(1, n):
        to_right[i] = gcd(a[i], to_right[i - 1])
    
    for i in range(n - 1, 0, -1):
        to_left[i - 1] = gcd(a[i - 1], to_left[i])
        
    ans = 1

    for i in range(n):
        left, right = -1, -1

        if i - 1 >= 0:
            left = to_right[i - 1]

        if i + 1 < n:
            right = to_left[i + 1]
        
        if left == -1:
            ans = max(ans, right)
        elif right == -1:
            ans = max(ans, left)
        else:
            ans = max(ans, gcd(left, right))
    
    print(ans)


if __name__ == "__main__":
    main()
