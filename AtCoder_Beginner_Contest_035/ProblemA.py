'''input
64 48
4:3

28 21
4:3

16 9
16:9

64 36
16:9

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    w, h = list(map(int, input().split()))

    if w * 9 == h * 16:
        print('16:9')
    elif w * 3 == h * 4:
        print('4:3')
