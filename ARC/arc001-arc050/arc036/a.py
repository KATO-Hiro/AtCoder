# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, k = list(map(int, input().split()))
    ts = list(accumulate([0] + [int(input()) for _ in range(n)]))

    for i in range(n - 3 + 1):
        if ts[i + 3] - ts[i] < k:
            print(i + 3)
            exit()

    print(-1)


if __name__ == '__main__':
    main()
