# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    c = Counter(b)
    x = int(input())
    x_max = 2 * 10 ** 5 + 10

    dp = [False] * x_max
    dp[0] = True

    for i in range(x):
        if not dp[i]:
            continue

        for aj in a:
            ni = i + aj

            if c[ni] != 1:
                dp[ni] = True
    
    if dp[x]:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()
