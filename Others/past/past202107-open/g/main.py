# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    i = 0
    powers = list()

    # See:
    # https://blog.hamayanhamayan.com/entry/2021/07/24/202945
    # シンプル、かつ、実装しやすいのルールに基づいて構築
    # nに近づくような値、かつ、同値の場合は絶対値が大きい方を選ぶ
    while 3**i <= 2 * 10**15:
        powers.append(3**i)
        i += 1

    ans = list()
    remain = n

    # n→0となるように
    for power in powers[::-1]:
        if abs(remain + power) < abs(remain):
            remain += power
            ans.append(-power)
        elif abs(remain - power) < abs(remain):
            remain -= power
            ans.append(power)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
