'''input
72
29
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    number = list(map(int, input()))

    if number.count(9):
        print('Yes')
    else:
        print('No')
