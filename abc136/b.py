# -*- coding: utf-8 -*-


def count_digit(n: int) -> int:
    digit = 0

    while n:
        digit += 1
        n //= 10

    return digit


def main():
    n = int(input())
    ans = 0

    for i in range(1, n + 1):
        if count_digit(i) % 2 == 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
