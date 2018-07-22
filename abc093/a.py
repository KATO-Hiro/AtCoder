'''input
bab
No

bac
Yes

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    s = input()

    if s.count('a') == 1 and s.count('b') == 1 and s.count('c') == 1:
        print('Yes')
    else:
        print('No')
