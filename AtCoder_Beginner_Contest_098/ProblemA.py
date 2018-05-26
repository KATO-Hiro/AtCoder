'''input
3 1
4
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    print(max(a + b, a - b, a * b))
