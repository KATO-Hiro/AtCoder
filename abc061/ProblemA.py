'''input
6 5 4
No

1 3 2
Yes

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, c = map(int, input().split())

    if a <= c <= b:
        print('Yes')
    else:
        print('No')
