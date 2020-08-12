'''input
FESTIVAL2016CODE
16

C0DEFESTIVAL2O16
2

'''

# -*- coding: utf-8 -*-

# CODE FESTIVAL 2016 qual A
# Problem A

if __name__ == '__main__':
    original = 'CODEFESTIVAL2016'
    s = input()
    count = 0

    for si, original_s in zip(s, original):
        if si != original_s:
            count += 1

    print(count)
