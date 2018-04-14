'''input
6
5 5 4 4 3 3
4
4
4
4
4
4

4
2 4 4 3
4
3
3
4

2
1 2
2
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    sorted_x = sorted(x)

    low = sorted_x[(n // 2) - 1]
    high = sorted_x[(n // 2)]

    for i in range(n):
        if x[i] < high:
            print(high)
        else:
            print(low)
