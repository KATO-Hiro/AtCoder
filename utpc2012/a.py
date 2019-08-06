# -*- coding: utf-8 -*-


def main():
    s = input()

    if sorted(s[1:5]) == sorted(s[6:8] + s[9:11]):
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
