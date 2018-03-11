'''input
3
4
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    N = int(input())
    white_count = int(input())

    black_count = N ** 2 - white_count
    print(black_count)
