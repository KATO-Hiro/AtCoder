'''input
hthth
No

abaccaba
Yes

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    from collections import Counter

    w = Counter(input())
    result = 'Yes'

    for count in w.values():
        if count % 2 != 0:
            print('No')
            exit()

    print(result)
