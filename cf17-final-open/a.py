# -*- coding: utf-8 -*-


def main():
    from re import search

    s = input()
    removed_a = s.replace('A', '')

    if (len(s) < 5 or len(s) < 10) and removed_a != 'KIHBR':
        print('NO')
    else:
        pattern = r'^A?KIHA?BA?RA?$'
        is_match = search(pattern, s)

        if is_match:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
