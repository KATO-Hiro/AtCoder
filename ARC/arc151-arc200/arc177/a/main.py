# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    counts = list(map(int, input().split()))[::-1]
    n = int(input())
    x = list(map(int, input().split()))
    coins = [1, 5, 10, 50, 100, 500][::-1]

    for xi in x:
        remain = xi

        for i, (coin, count) in enumerate(zip(coins, counts)):
            use = min(count, remain // coin)
            remain -= use * coin
            counts[i] -= use

        if remain != 0:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
