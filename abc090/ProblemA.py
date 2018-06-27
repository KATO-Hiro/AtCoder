'''input
ant
obe
rec
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    strings = [list(map(str, input())) for _ in range(3)]
    print(strings[0][0] + strings[1][1] + strings[2][2])
