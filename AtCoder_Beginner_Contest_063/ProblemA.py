'''input
6 4
error

6 3
9

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    total = a + b
    if total < 10:
        print(total)
    else:
        print('error')
