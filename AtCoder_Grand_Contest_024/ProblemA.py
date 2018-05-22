'''input
1000000000 1000000000 1000000000 1000000000000000000
0

1 2 3 1
1

2 3 2 0
-1

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    a, b, c, k = list(map(int, input().split()))

    if k % 2 == 0:
        print(a - b)
    else:
        print(b - a)
