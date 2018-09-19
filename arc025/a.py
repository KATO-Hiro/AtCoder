# -*- coding: utf-8 -*-


def main():
    d = list(map(int, input().split()))
    j = list(map(int, input().split()))
    gold_amount = 0

    for di, ji in zip(d, j):
        gold_amount += max(di, ji)

    print(gold_amount)


if __name__ == '__main__':
    main()
