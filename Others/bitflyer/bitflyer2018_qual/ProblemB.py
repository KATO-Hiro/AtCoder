'''input
100 99 9
SSSEEECCC
96
94

3 2 3
SEC
1
1

2 4 6
SSSEEE
0
1

0 3 6
SEECEE
0
0

'''

# -*- coding: utf-8 -*-

# bitflyer2018 qual
# Problem B

if __name__ == '__main__':
    a, b, n = list(map(int, input().split()))
    x = input()

    for xi in x:
        if xi == 'S' and a > 0:
            a -= 1
        elif xi == 'C' and b > 0:
            b -= 1
        elif xi == 'E':
            if a >= b and a > 0:
                a -= 1
            elif a < b and b > 0:
                b -= 1

    print(a)
    print(b)
