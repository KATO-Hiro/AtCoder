'''input
14000000 2458 692196
0

100 40 35
0

100 60 70
30

'''

# -*- coding: utf-8 -*-

# DWANGO #3 qual
# Problem A

if __name__ == '__main__':
    n, a, b = list(map(int, input().split()))

    print(max(0, (a + b) - n))
