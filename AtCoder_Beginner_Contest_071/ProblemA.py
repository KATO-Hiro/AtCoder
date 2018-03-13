'''input
1 999 1000
A
5 2 7
B
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    x, a, b = list(map(int, input().split()))

    if abs(x - a) < abs(x - b):
        print('A')
    else:
        print('B')
