'''input
1 21
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B
import math


if __name__ == '__main__':
    a, b = map(str, input().split(" "))

    number = int(a + b)
    root_number = math.sqrt(number)

    if abs(number - int(root_number) ** 2) < 10 ** -6:
        print("Yes")
    else:
        print("No")
