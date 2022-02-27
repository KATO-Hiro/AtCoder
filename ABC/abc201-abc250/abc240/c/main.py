# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    ab = list()

    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, bi))
    
    dp = [False] * (x + 1)
    dp[0] = True

    for j in range(n):
        ndp = [False] * (x + 1)

        for i in range(x + 1):
            if dp[i]:
                if i + ab[j][0] <= x:
                    ndp[i + ab[j][0]] = True
                if i + ab[j][1] <= x:
                    ndp[i + ab[j][1]] = True

        dp = ndp
    
    if dp[x]:
        print("Yes")
    else:
        print("No")    


if __name__ == "__main__":
    main()
