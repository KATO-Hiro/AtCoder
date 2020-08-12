'''input
1881
No

2525
Yes

'''

# -*- coding: utf-8 -*-

# DWANGO #4 qual
# Problem A

if __name__ == '__main__':
    s = input()

    if s[:2] == s[2:]:
        print('Yes')
    else:
        print('No')
