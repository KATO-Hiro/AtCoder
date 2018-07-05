'''input
10 4
2 7 22
3 5 4
6 10 1
4 4 12

0
22
4
12
4
1
1
1
1
1

5 2
1 3 10
2 4 20

10
20
20
20
0

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n, q = list(map(int, input().split()))
    a = [0 for _ in range(n)]

    for i in range(q):
        l, r, t = list(map(int, input().split()))
        l -= 1

        for j in range(l, r):
            a[j] = t

    for ai in a:
        print(ai)
