'''input
3
cbaa
daacc
acacac
aac

3
a
aa
b


'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    from collections import Counter

    n = int(input())
    tmp = Counter(input())

    for i in range(n - 1):
        tmp = tmp & Counter(input())

    print(''.join(sorted(list(tmp.elements()))))
