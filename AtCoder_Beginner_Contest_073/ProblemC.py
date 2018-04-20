'''input
4
2
5
5
2
0

6
12
22
16
22
18
12
2

3
6
2
6
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    from collections import Counter

    n = int(input())
    a = [0] * n
    count = 0

    for i in range(n):
        a[i] = int(input())

    for key, value in Counter(a).items():
        if value % 2 != 0:
            count += 1

    print(count)
