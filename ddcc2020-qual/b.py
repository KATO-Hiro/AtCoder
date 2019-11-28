# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n = int(input())
    a = list(accumulate([0] + list(map(int, input().split()))))
    ans = float('inf')

    for i in range(1, n + 1):
        ans = min(ans, abs((a[n] - a[i]) - a[i]))

    print(ans)


if __name__ == '__main__':
    main()
