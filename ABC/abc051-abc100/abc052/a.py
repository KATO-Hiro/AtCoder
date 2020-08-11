'''input
3 5 2 7
15

100 600 200 300
60000

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))
    print(max(a * b, c * d))
