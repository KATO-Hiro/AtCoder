'''input
1 1
Impossible

4 5
Possible

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    if (a % 3 == 0) or (b % 3 == 0) or ((a + b) % 3 == 0):
        print('Possible')
    else:
        print('Impossible')
