# -*- coding: utf-8 -*-


def main():
    from fractions import gcd

    n, large_x = map(int, input().split())
    x = sorted(list(map(int, input().split())) + [large_x])
    ans = float('inf')

    if len(x) == 2:
        print(x[1] - x[0])
        exit()

    for k in range(n - 1):
        ans = min(ans, gcd(x[k + 2] - x[k + 1], x[k + 1] - x[k]))

    print(ans)


if __name__ == '__main__':
    main()
