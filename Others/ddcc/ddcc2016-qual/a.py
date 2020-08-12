'''input
90 120 100
133.3333333333333333

2 3 5
7.5000000000000000

'''

# -*- coding: utf-8 -*-

# ddcc2016 qual
# Problem A

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))
    print(b / a * c)
