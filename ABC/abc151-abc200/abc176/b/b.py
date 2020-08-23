# -*- coding: utf-8 -*-


def main():
    s = input()
    total = 0

    for si in s:
        total += int(si)

    if total % 9 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
