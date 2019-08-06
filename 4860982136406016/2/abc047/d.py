# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    minmum_numbers = [a[0] for _ in range(n)]
    diff = [0 for _ in range(n)]

    for i in range(1, n):
        minmum_numbers[i] = min(minmum_numbers[i - 1], a[i])
        diff[i] = a[i] - minmum_numbers[i]

    print(sorted(Counter(diff).items(), key=lambda x: x[0], reverse=True)[0][1])


if __name__ == '__main__':
    main()
