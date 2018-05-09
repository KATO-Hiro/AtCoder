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
    s = input()
    cf = 'CF'
    count = 0

    for si in s:
        if count == 0 and si == cf[0]:
            count += 1
        elif count == 1 and si == cf[1]:
            print('Yes')
            exit()

    print('No')
