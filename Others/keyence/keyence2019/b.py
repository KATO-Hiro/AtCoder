# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)

    for i in range(n):
        for k in range(i, n):
            if (s[:i] + s[k:]) == 'keyence':
                print('YES')
                exit()

    print('NO')


if __name__ == '__main__':
    main()
