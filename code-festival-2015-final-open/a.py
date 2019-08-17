# -*- coding: utf-8 -*-


def main():
    s, t, u = map(str, input().split())

    if len(s) == 5 and len(t) == 7 and len(u) == 5:
        print('valid')
    else:
        print('invalid')


if __name__ == '__main__':
    main()
