'''input
2 3 4
52

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))
    print(2 * (a * b + b * c + c * a))
