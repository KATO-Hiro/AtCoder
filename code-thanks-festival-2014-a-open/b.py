# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    numbers = sorted([a, b, c], reverse=True) * 334
    ans = 0

    for number in numbers:
        n -= number
        ans += 1

        if n <= 0:
            print(ans)
            exit()


if __name__ == '__main__':
    main()
