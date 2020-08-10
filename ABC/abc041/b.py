'''input
1000000000 1000000000 1000000000
999999664

2 3 4
24

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))
    print((a * b * c) % (10 ** 9 + 7))
