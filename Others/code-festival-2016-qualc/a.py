'''input
CF
Yes

CODEFESTIVAL
Yes

FESTIVALCODE
No

'''

# -*- coding: utf-8 -*-

# CODE FESTIVAL 2016 qual C
# Problem A

if __name__ == '__main__':
    import re
    s = input()

    # See:
    # https://beta.atcoder.jp/contests/code-festival-2016-qualc/submissions/942114
    if re.search('C.*F', s):
        print('Yes')
    else:
        print('No')
