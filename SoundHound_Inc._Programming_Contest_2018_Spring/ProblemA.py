'''input
SOUND SPIDER
NO

SAINT HELENA
YES

'''

# -*- coding: utf-8 -*-

# SoundHound Inc. Programming Contest 2018 Spring
# Problem A

if __name__ == '__main__':
    x, y = list(map(str, input().split()))

    if x[0] + y[0] == 'SH':
        print('YES')
    else:
        print('NO')
