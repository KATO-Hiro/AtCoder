# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0
    coins = [500, 100, 50, 10, 5, 1]

    for i in range(n):
        ai, bi = map(int, input().split())
        diff = bi - ai

        for coin in coins:
            if diff > 0:
                p, q = divmod(diff, coin)

                if coin == 5 or coin == 50:
                    ans += p

                diff = q

    print(ans)

if __name__ == "__main__":
    main()
