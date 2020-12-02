# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_right
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    h = sorted(list(map(int, input().split())))
    w = list(map(int, input().split()))

    summed_h = [0 for _ in range(n + 1)]

    for index, hi in enumerate(h, 1):
        if index % 2 == 1:
            summed_h[index] -= hi
        else:
            summed_h[index] += hi

        summed_h[index] += summed_h[index - 1]

    ans = float("Inf")

    for wi in w:
        index = bisect_right(h, wi)

        if index % 2 == 0:
            flag = -1
        else:
            flag = 1

        total = summed_h[index]
        total += flag * wi
        total -= summed_h[n] - summed_h[index]

        ans = min(ans, total)

    print(ans)


if __name__ == "__main__":
    main()
