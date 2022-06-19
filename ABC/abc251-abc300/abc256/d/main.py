# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    size_max = 2 * 10 ** 5 + 100
    imos = [0] * (size_max)

    for i in range(n):
        li, ri = map(int, input().split())
        imos[li] += 1
        imos[ri] -= 1
    
    imos = list(accumulate(imos))
    start = False
    ans = list()

    for i, value in enumerate(imos):
        if not start and value >= 1:
            start = True
            ans.append(i)
        elif start and value == 0:
            start = False
            ans.append(i)

    size = len(ans) // 2
    
    for i in range(size):
        print(ans[2 * i], ans[2 * i + 1])


if __name__ == "__main__":
    main()
