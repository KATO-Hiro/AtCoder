'''input
98 56
Worse

12 34
Better

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    x, y = list(map(int, input().split()))

    if x < y:
        print('Better')
    else:
        print('Worse')
