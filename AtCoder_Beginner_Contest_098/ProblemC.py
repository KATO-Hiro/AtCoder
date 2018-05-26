'''input
12
WEWEWEEEWWWE
4

8
WWWWWEEE
3

5
WEEWW
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    s = input()
    count = 0
    ws = [0] * n
    es = [0] * n

    for i in range(0, n):
        if s[i] == 'W':
            ws[i] = ws[i - 1] + 1
            es[i] = es[i - 1]
        else:
            es[i] = es[i - 1] + 1
            ws[i] = ws[i - 1]

    for i in range(len(s) - 1):
        if i == 0:
            count = es[-1] - es[1]
        else:
            count = min(count, (ws[i]) + (es[-1] - es[i + 1]))

    print(count)
