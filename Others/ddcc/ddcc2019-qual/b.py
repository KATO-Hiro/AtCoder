# -*- coding: utf-8 -*-


def main():
    n = int(input())

    if n % 2 == 0:
        ans = 0

        for i in range(2, n // 2 + 1):
            ans += 4 * i - 4
    else:
        ans = 1

        for i in range(2, n // 2 + 1):
            ans += 4 * i - 4

    print(ans)


if __name__ == '__main__':
    main()
