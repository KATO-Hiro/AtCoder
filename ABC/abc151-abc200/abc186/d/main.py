# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)

    summed_a = list(accumulate([0] + a))
    ans = 0

    for index, ai in enumerate(a):
        ans += ai * (n - index - 1)
        ans -= summed_a[n] - summed_a[index + 1]

    print(ans)


if __name__ == "__main__":
    main()
