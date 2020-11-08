# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    max_value = 10 ** 6
    numbers = [0 for _ in range(max_value + 10)]

    # 数列に含まれる値がいくつあるか数える
    for ai in a:
        numbers[ai] += 1

    for i in range(1, max_value + 1):
        # 割り切れる⇄倍数と言い換え
        # エラトステネスの篩のようなイメージで、倍数を答えから除外する
        # 何回か同じ倍数に対して操作をしているため、やや効率が悪い
        if numbers[i] > 0:
            for j in range(2 * i, max_value + 1, i):
                numbers[j] = 0

        # 同じ数が2個以上ある場合は0に
        if numbers[i] >= 2:
            numbers[i] = 0

    print(sum(numbers))


if __name__ == "__main__":
    main()
