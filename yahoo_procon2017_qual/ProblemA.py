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
    s = input()

    if s.count('y') == 1 and s.count('a') == 1 and s.count('h') == 1 and s.count('o') == 2:
        print('YES')
    else:
        print('NO')
