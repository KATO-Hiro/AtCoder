'''input
E C
A B
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    X, Y = list(map(str, input().split()))
    HEX = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    X_value = HEX[X]
    Y_value = HEX[Y]

    if X_value > Y_value:
        print('>')
    elif X_value < Y_value:
        print('<')
    else:
        print('=')
