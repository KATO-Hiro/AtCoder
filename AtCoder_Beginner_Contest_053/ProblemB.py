'''input
ZABCZ
4

HASFJGHOGAKZZFEGA
12

QWERTYASDFZXCV
5

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    s = list(input())
    a_position = s.index('A')
    z_position = len(s) - s[::-1].index('Z') - 1

    print(z_position - a_position + 1)
