# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate
    from math import ceil

    input = sys.stdin.readline

    n, d, p = map(int, input().split())
    f = sorted(list(map(int, input().split())), reverse=True)
    acc = [0] + list(accumulate(f))
    # print(acc)

    f_sum = sum(f)
    ans = min(f_sum, ceil(n / d) * p)
    i = 1

    while True:
        j = min(i * d, n)

        candidate = f_sum - acc[j] + (i * p)
        # print(f_sum, acc[j], i * d, candidate)
        ans = min(ans, candidate)

        i += 1

        if i * d > n:
            break

    print(ans)


if __name__ == "__main__":
    main()
