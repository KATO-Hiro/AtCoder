'''input
50 100 120
Yes

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    A, B, C = list(map(int, input().split()))

    if (A + B) >= C:
        print('Yes')
    else:
        print('No')
