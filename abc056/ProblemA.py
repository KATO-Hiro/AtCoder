'''input
D D
H

H H
H

D H
D

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b = input().split()

    if a == b:
        print('H')
    else:
        print('D')
