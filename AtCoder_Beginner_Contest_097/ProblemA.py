'''input
1 100 2 10
Yes

10 10 10 1
Yes

4 7 9 3
Yes

100 10 1 2
No

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))

    if abs(a - b) <= d and abs(b - c) <= d:
        print('Yes')
    elif abs(a - c) <= d:
        print('Yes')
    else:
        print('No')
