'''input
5
IIDID
2

7
DDIDDII
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    n = int(input())
    s = input()

    x = 0
    result = 0

    for si in s:
        if si == 'I':
            x += 1
            result = max(x, result)
        elif si == 'D':
            x -= 1
            result = max(x, result)

    print(result)