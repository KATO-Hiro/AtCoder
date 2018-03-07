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

    A, B = list(map(int, input().split()))
    S = str(input())

    # XXX: pattern is something wrong.
    text = r'(\d{{0}})\-(\d{{1}})'.format(A, B)
    pattern = re.compile(text)
    result = pattern.search(S)

    if result:
        print("Yes")
    else:
        print("No")
