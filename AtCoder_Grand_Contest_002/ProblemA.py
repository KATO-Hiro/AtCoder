'''input
-1000000000 1000000000
Zero

-1 0
Zero

1 3
Positive

-3 -1
Negative

-4 -1
Positive

-1 1
Zero

0 1
Zero

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    if a >= 1:
        print('Positive')
    elif a * b <= 0:
        print('Zero')
    elif b <= -1:
        if (a - b + 1) % 2 == 0:
            print('Positive')
        else:
            print('Negative')
