# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = [0] * n
    used = [False] * n
    mod = 998244353

    for _ in range(k):
        ci, ki = input().split()
        ki = int(ki)
        used[ki - 1] = True

        if ci == "L":
            start = ki
            end = n
        else:
            start = 0
            end = ki - 1
        
        for i in range(start, end):
            a[i] += 1
    
    ans = 1

    for index, ai in enumerate(a):
        if not used[index]:
            ans *= ai
            ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
