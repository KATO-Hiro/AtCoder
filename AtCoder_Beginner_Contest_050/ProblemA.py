'''input
1 + 2
3

5 - 7
-2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, op, b = input().split()

    if op == '+':
        print(int(a) + int(b))
    else:
        print(int(a) - int(b))
