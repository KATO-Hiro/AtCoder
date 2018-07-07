# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input()
    w = int(input())
    print(''.join(map(str, s[::w])))
