# -*- coding: utf-8 -*-


def count_coins(total, order, ans):
    if order == 0:
        return ans + total

    order -= 1
    add = total // (10 ** order)
    add -= 4 * (add // 5)
    return count_coins(total % (10 ** order), order, ans + add)


def main():
    from itertools import combinations

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    prices = list()

    for i in combinations(a, k):
        prices.append(sum(i))

    ans = float('inf')

    for price in prices:
        ans = min(ans, count_coins(price, 9, 0))

    print(ans)


if __name__ == '__main__':
    main()
