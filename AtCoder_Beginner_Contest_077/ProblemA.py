'''input
pot
top
tab
bet
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    c = [input() for _ in range(2)]

    if (c[0][0] == c[1][2]) and (c[1][0] == c[0][2]) and (c[0][1] == c[1][1]):
        print('YES')
    else:
        print('NO')
