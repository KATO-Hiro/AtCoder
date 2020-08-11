'''input
SSTTST
0

TSSTTTSS
4

TSTTSS
4

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    from collections import deque

    x = input()
    n = len(x)
    d = deque()

    for i in range(n):
        d.append(x[i])

        if len(d) >= 2 and d[-2] + d[-1] == 'ST':
            d.pop()
            d.pop()

    print(len(d))
