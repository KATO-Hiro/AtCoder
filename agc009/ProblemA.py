'''input
7
3 1
4 1
5 9
2 6
5 3
5 8
9 7
22

3
3 5
2 7
9 4
7

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    n = int(input())
    ab = [None] * n
    count = 0

    for i in range(n):
        ab[i] = list(map(int, input().split()))

    for k in range(n - 1, -1, -1):
        q = (count + ab[k][0]) % ab[k][1]

        if q > 0:
            count += ab[k][1] - q

    print(count)
