'''input
100
64

7
4

32
32

1
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    number = int(input())

    count = 0

    while 2 ** count <= number:
        count += 1

    print(2 ** (count - 1))
