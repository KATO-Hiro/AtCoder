# -*- coding: utf-8 -*-


def main():
    n = input()
    ans = ''

    for ni in n:
        if ni == '1':
            ans += '9'
        elif ni == '9':
            ans += '1'

    print(ans)


if __name__ == '__main__':
    main()
