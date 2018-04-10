'''input
3 3 33
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    paint_cans = list(map(int, input().split()))
    print(len(set(paint_cans)))
