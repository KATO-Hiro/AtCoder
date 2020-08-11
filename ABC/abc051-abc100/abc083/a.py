'''input
3 8 7 1
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    A, B, C, D = list(map(int, input().split()))

    left_weight = A + B
    right_weight = C + D

    if left_weight > right_weight:
        print("Left")
    elif left_weight == right_weight:
        print("Balanced")
    else:
        print("Right")
