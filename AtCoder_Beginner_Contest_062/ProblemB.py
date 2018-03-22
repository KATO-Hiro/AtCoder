'''input
1 1
z

###
#z#
###

2 3
abc
arc

#####
#abc#
#arc#
#####

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    height, width = map(int, input().split())
    header = ''

    for _ in range(width + 2):
        header += header.join('#')

    print(header)

    for i in range(height):
        line = input()
        print('#' + line + '#')

    print(header)
