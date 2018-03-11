'''input
1 1
314 1592
496080
6 1
1 7
5
2 2
0
3 3
1
4 4
4
5 5
9
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    N, M = list(map(int, input().split()))

    if N == 1 and M == 1:
        print(1)
    elif N == 1:
        print(M - 2)
    elif M == 1:
        print(N - 2)
    else:
        print((N - 2) * (M - 2))
