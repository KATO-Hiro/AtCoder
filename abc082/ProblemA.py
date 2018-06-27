'''input
5 5
5
'''

'''input
7 4
6
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    A, B = list(map(int, input().split()))

    mean = (A + B + 1) // 2
    print(mean)
