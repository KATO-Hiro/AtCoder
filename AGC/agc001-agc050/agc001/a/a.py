'''input
5
100 1 2 3 14 15 58 58 58 29
135

2
1 3 1 2
3

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    number = int(input())
    l = sorted(list(map(int, input().split())), reverse=True)
    count = 0

    for i in range(number):
        count += min(l[2 * i], l[2 * i + 1])

    print(count)
