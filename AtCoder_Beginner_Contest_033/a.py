# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = list(map(int, input()))

    if len(set(n)) == 1:
        print('SAME')
    else:
        print('DIFFERENT')
