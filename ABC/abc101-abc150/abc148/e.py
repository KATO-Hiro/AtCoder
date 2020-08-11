# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = 0

    if n % 2 == 1:
        print(ans)
    else:
        division = 10

        while division <= n:
            ans += n // division

            division *= 5

        print(ans)


if __name__ == '__main__':
    main()
