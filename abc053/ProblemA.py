'''input
1200
ARC

2000
ARC

1000
ABC

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    rate = int(input())

    if rate < 1200:
        print('ABC')
    else:
        print('ARC')
