# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [0] * (n + 1)

    if n >= 3:
        a[2] = 1

        for i in range(3, n):
            a[i] = a[i - 1] + a[i - 2] + a[i - 3]
            a[i] %= 10007

    print(a[n - 1])


if __name__ == '__main__':
    main()
