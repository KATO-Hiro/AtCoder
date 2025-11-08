# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    orders = list()

    for i in range(n):
        name, time = input().rstrip().split()
        time = int(time)

        if name != "Takahashi":
            continue

        orders.append((time, i + 1))

    orders.sort()
    print(orders[0][1])


if __name__ == "__main__":
    main()
