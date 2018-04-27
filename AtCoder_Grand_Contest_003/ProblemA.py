'''input
SEN
No

W
No

SENW
Yes

NSNNSNSN
Yes

NNEW
No

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    from collections import Counter

    s = Counter(input())

    # See:
    # http://agc003.contest.atcoder.jp/data/agc/003/editorial.pdf
    if ('S' in s.keys()) and ('N' not in s.keys()):
        print('No')
    elif ('N' in s.keys()) and ('S' not in s.keys()):
        print('No')
    elif ('W' in s.keys()) and ('E' not in s.keys()):
        print('No')
    elif ('E' in s.keys()) and ('W' not in s.keys()):
        print('No')
    else:
        print('Yes')
