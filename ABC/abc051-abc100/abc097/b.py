'''input
999
961

10
9

1
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    x = int(input())
    value = 0

    for i in range(100):
        for j in range(2, 10):
            tmp = pow(i, j)
            if tmp <= x and tmp > value:
                value = tmp

    print(value)
