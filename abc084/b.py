'''input
3 4
269-6650
'''
'''input
1 1
1 2
7444
---
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    import re

    A, B = list(map(str, input().split()))
    S = str(input())

    # See:
    # https://beta.atcoder.jp/contests/abc084/submissions/1936327
    text = r'\d{' + A + '}\-\d{' + B + '}'
    result = re.match(text, S)

    if result:
        print("Yes")
    else:
        print("No")
