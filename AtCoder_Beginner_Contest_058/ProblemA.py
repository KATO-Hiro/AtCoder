'''input
2 4 6
YES

2 5 6
NO

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))

    if (b - a) == (c - b):
        print('YES')
    else:
        print('NO')
