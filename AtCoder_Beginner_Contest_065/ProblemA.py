'''input
3 7 12
dangerous

4 3 6
safe

6 5 1
delicious

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    x, a, b = list(map(int, input().split()))

    if (x + a + 1) <= b:
        print('dangerous')
    elif a < b <= (x + a):
        print('safe')
    else:
        print('delicious')
