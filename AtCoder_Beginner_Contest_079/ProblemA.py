'''input
7777
1234
1101
1118
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    number = list(map(int, input()))

    for i in range(0, 10):
        if (number.count(i) >= 3) and (number[1] == i and number[2] == i):
            print('Yes')
            break
    else:
        print('No')
