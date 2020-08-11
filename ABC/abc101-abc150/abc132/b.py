# -*- coding: utf-8 -*-


def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0

    for i in range(1, n - 1):
        value_max = max(p[i - 1], p[i], p[i + 1])
        value_min = min(p[i - 1], p[i], p[i + 1])

        if p[i] != value_max and p[i] != value_min:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
