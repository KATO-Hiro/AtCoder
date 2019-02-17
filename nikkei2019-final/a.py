# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n = int(input())
    a = list(accumulate([0] + list(map(int, input().split()))))

    for i in range(1, n + 1):
        ans = 0

        for k in range(n - (i - 1)):
            ans = max(ans, a[k + i] - a[k])

        print(ans)


if __name__ == '__main__':
    main()
