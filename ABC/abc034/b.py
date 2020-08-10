'''input
123456789
123456790

100
99

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = int(input())

    if n % 2 == 0:
        n -= 1
    else:
        n += 1

    print(n)
