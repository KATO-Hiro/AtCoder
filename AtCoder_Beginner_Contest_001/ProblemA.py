# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 001
# Problem A
# Difference in snow depth.

if __name__ == '__main__':
    height = int(input())
    height_previous_hour = int(input())

    diff = height - height_previous_hour
    print(diff)

