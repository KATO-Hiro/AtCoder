'''input
271828182
271821169
10
9
81
81
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    import math

    number = int(input())
    sqrt_number = int(math.sqrt(number))
    result = sqrt_number ** 2
    print(result)
