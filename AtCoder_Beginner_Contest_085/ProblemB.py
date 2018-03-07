'''input
7
50
30
50
100
50
80
30
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    mochi_count = int(input())
    mochi_diameters = [int(input()) for _ in range(mochi_count)]

    step_count = len(set(mochi_diameters))
    print(step_count)
