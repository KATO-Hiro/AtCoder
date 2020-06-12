# -*- coding: utf-8 -*-


def main():
    s = input()
    t = input()

    if s == t:
        print('same')
    elif s.lower() == t.lower():
        print('case-insensitive')
    else:
        print('different')


if __name__ == '__main__':
    main()
