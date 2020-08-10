'''input
5
3
10000
9000
48000

2
3
10000
9000
20000

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    diff = n - k

    if diff > 0:
        print((k * x) + diff * y)
    else:
        print(n * x)
