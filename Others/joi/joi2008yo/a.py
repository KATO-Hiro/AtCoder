# -*- coding: utf-8 -*-


def main():
    n = 1000 - int(input())
    coins = [500, 100, 50, 10, 5, 1]
    ans = 0

    for coin in coins:
        p, q = divmod(n, coin)
        ans += p
        n = q

    print(ans)


if __name__ == '__main__':
    main()
