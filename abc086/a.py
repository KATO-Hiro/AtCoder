'''input
3 4
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b = map(int, input().split(" "))

    result = (a * b) % 2

    if result == 0:
        print("Even")
    else:
        print("Odd")
