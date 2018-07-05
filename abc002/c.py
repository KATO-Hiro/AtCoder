'''input
298 520 903 520 4 663
43257.5

1 0 3 0 2 5
5.0

-1 -2 3 4 5 6
2.0

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    xa, ya, xb, yb, xc, yc = list(map(int, input().split()))
    print(abs((xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)) / 2)
