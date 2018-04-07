'''input
4 8 3
4
5
6
7
8


3 8 2
3
4
7
8

2 9 100
2
3
4
5
6
7
8
9

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    a, b, k = list(map(int, input().split()))

    if (b - a + 1) <= 2 * k:
        for i in range(a, b + 1):
            print(i)
    else:
        for j in range(a, a + k):
            print(j)
        for j in range(b - k + 1, b + 1):
            print(j)
