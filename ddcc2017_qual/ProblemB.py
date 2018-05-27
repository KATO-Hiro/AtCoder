'''input
1 2 4 0
2064

'''

# -*- coding: utf-8 -*-

# ddcc2017 qual
# Problem B

if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))
    print(1728 * a + 144 * b + 12 * c + d)
