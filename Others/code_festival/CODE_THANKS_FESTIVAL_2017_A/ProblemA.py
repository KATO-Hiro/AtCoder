'''input
240
600
1800
3600
4800
7200
10000
0
10000

10400
10300
10100
9800
9500
8500
7000
5000
10400

0
0
0
0
0
0
0
0
0

'''

# -*- coding: utf-8 -*-

# CODE THANKS FESTIVAL 2017 A
# Problem A

if __name__ == '__main__':
    ts = [int(input()) for _ in range(8)]
    print(max(ts))
