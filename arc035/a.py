# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)

    for i in range(n):
        if s[i] == s[n - i - 1]:
            pass
        elif s[i] == '*' or s[n - i - 1] == '*':
            pass
        else:
            print('NO')
            exit()

    print('YES')


if __name__ == '__main__':
    main()
