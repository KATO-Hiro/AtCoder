# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    # 各操作で1つはai % 2 == 0である必要がある
    # 操作回数 = aiが2で何回割り切れるか
    for ai in a:
        while ai % 2 == 0:
            ai //= 2
            count += 1

    print(count)


if __name__ == "__main__":
    main()
