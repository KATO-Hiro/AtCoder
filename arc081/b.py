# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [input() for _ in range(2)]
    mod = 10 ** 9 + 7
    ans = 1
    i = 0

    if s[0][0] == s[1][0]:
        ans *= 3
        i = 1
    else:
        ans *= 6
        i = 2

    while i < n:
        if s[0][i] == s[1][i]:
            if s[0][i - 1] == s[1][i - 1]:
                ans *= 2

            i += 1
        else:
            if s[0][i - 1] == s[1][i - 1]:
                ans *= 2
            else:
                ans *= 3

            i += 2

        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
