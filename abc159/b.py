# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)

    if s == s[::-1]:
        t = s[:(n - 1) // 2]
        u = s[(n + 3) // 2 - 1:]

        if t == t[::-1] and u == u[::-1]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


if __name__ == '__main__':
    main()
