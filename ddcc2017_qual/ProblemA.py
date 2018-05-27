'''input
ABCD
No

DDCC
Yes

'''

# -*- coding: utf-8 -*-

# ddcc2017 qual
# Problem A

if __name__ == '__main__':
    s = input()

    if s[0] == s[1] and s[1] != s[2] and s[2] == s[3]:
        print('Yes')
    else:
        print('No')
