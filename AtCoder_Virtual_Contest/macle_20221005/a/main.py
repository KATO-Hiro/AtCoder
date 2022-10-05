# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    p = int(input())
    coins = list()
    tmp = 1

    for i in range(1, 10 + 1):
        tmp *= i
        coins.append(tmp)
    
    ans = 0

    for coin in coins[::-1]:
        a, b = divmod(p, coin)
        count = min(a, 100)

        p -= count * coin
        ans += count

        if p == 0:
            print(ans)
            exit()

        if a > 100:
            b += (a - 100) * coin


if __name__ == "__main__":
    main()
