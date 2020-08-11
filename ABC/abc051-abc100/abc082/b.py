'''input
atcoder
atlas

yx
axy

ratcode
atlas
Yes

cd
abc
No

w
ww
Yes

zzz
zzz
No
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B


if __name__ == '__main__':
    s = sorted(list(input()))
    t = sorted(list(input()), reverse=True)

    if s < t:
        print('Yes')
    else:
        print('No')
