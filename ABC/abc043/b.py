'''input
0BB1
1

01B0
00

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    s = input()
    result = ''

    for si in s:
        if si == '0' or si == '1':
            result += si
        elif si == 'B':
            if len(result) != 0:
                result = result[:len(result) - 1]

    print(result)
