# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = [int(si == "B") for si in s]

    acc_t = list(accumulate(t))
    a = [int(i % 2 == 1) for i in range(2 * n)]
    acc_a = list(accumulate(a))
    b = [int(i % 2 == 0) for i in range(2 * n)]
    acc_b = list(accumulate(b))
    ans1, ans2 = 0, 0

    for acc_ti, acc_ai in zip(acc_t, acc_a):
        ans1 += abs(acc_ti - acc_ai)

    for acc_ti, acc_bi in zip(acc_t, acc_b):
        ans2 += abs(acc_ti - acc_bi)

    print(min(ans1, ans2))


if __name__ == "__main__":
    main()
