'''input
6 4
2

5 2
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    n, x = list(map(int, input().split()))
    print(min(x - 1, n - x))
