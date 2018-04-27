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
    s = input()

    # See:
    # http://agc003.contest.atcoder.jp/data/agc/003/editorial.pdf
    # https://beta.atcoder.jp/contests/agc003/submissions/849782
    if (('S' in s) ^ ('N' in s)) or (('W' in s) ^ ('E' in s)):
        print('No')
    else:
        print('Yes')
