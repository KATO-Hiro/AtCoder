# -*- coding: utf-8 -*-


def main():
    from string import ascii_lowercase
    import sys
    input = sys.stdin.readline

    n = int(input())
    ans = ''
    alpha = list(ascii_lowercase)

    while n >= 26:
        p, q = divmod(n, 26)

        ans += alpha[q - 1]
        n = p

        if q == 0:
            n -= 1

    if 0 < n < 26:
        ans += alpha[n - 1]

    print(ans[::-1])


if __name__ == '__main__':
    main()
