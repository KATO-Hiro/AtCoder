'''input
5 3 2
N

3 5 4
YES

2 2 6
NO

'''

# xxx = list(map(int, input().split()))

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, x = list(map(int, input().split()))

    if a <= x <= a + b:
        print('YES')
    else:
        print('NO')
