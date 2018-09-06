# -*- coding: utf-8 -*-


def main():
    from re import search

    s = input()
    pattern = r'^A?KIHA?BA?RA?$'
    is_match = search(pattern, s)

    if is_match:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
