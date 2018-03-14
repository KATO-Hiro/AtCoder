'''input
3 4
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    if (a * b) % 2 == 0:
        print("Even")
    else:
        print("Odd")
