# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    zero = [0 for _ in range(n)]
    one = [0 for _ in range(n)]
    ans = n + 100

    for index, ai in enumerate(a):
        if ai == 0:
            zero[index] += 1
        else:
            one[index] += 1

    zero = list(accumulate([0] + zero))
    one = list(accumulate([0] + one))

    for r in range(n + 1):
        cost = zero[r]
        cost += one[n] - one[r]

        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()
