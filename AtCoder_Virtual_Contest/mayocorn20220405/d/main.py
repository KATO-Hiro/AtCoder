# -*- coding: utf-8 -*-


def main():
    from math import gcd
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    to_right = [a[0]]
    to_left = [a[-1]]

    for i, ai in enumerate(a[1:], 1):
        to_right.append(gcd(to_right[i - 1], ai))
    
    for i, ai in enumerate(a[:-1][::-1]):
        to_left.append(gcd(to_left[-1], ai))
    
    to_left = to_left[::-1]
    ans = 1

    for i in range(n):
        if i == 0:
            ans = max(ans, to_left[i + 1])
        elif i == n - 1:
            ans = max(ans, to_right[i - 1])
        else:
            ans = max(ans, gcd(to_right[i - 1], to_left[i + 1]))

    print(ans)


if __name__ == "__main__":
    main()
