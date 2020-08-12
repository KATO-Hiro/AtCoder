'''input
yohaa
NO

oohay
YES

'''

# -*- coding: utf-8 -*-

# yahoo procon2017 qual
# Problem A

if __name__ == '__main__':
    s = sorted(input())
    yahoo = sorted('yahoo')

    if s == yahoo:
        print('YES')
    else:
        print('NO')
