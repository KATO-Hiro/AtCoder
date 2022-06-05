# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for i in range(1, n + 1):
        k = i
        d = 2

        # kのうち平方数となっていない部分を見つけるイメージ?
        while d ** 2 <= k:
            while k % (d ** 2) == 0:
                k /= d ** 2
            
            d += 1
        
        d = 1

        # 平方数となるものだけを数える
        while k * (d ** 2) <= n:
            ans += 1
            d += 1
        
    print(ans)


if __name__ == "__main__":
    main()
