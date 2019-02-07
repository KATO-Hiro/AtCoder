# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for i in range(n - 1):
        ans += a[i + 1] - a[i]

    print(ans / (n - 1))


if __name__ == '__main__':
    main()
