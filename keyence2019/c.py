# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    plus = list()
    minus = list()

    for ai, bi in zip(a, b):
        diff = ai - bi

        if diff > 0:
            plus.append(diff)
        elif diff < 0:
            minus.append(diff)

    sorted_plus = list(accumulate([0] + sorted(plus, reverse=True)))
    summed_plus = sorted_plus[-1]
    summed_minus = sum(minus)
    ans = len(minus)

    if summed_plus < abs(summed_minus):
        print(-1)
        exit()

    for i in range(len(sorted_plus)):
        summed = sorted_plus[i] - sorted_plus[0]

        if summed + summed_minus >= 0:
            print(ans)
            exit()

        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
