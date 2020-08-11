# -*- coding: utf-8 -*-


def main():
    from fractions import gcd
    from functools import reduce

    n, large_x = map(int, input().split())
    x = sorted(list(map(lambda x: int(x) - large_x, input().split())) + [0])
    diff = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        diff[i] = x[i] - x[i - 1]

    ans = reduce(gcd, diff)
    print(ans)


if __name__ == '__main__':
    main()
