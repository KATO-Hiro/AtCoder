'''input
10 8
322828856

2 2
2

1 10
10

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(k * ((k - 1) ** (n - 1)))
