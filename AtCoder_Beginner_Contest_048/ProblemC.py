'''input
5 9
3 1 4 1 5
0

3 2
4 6 4
10

2 0
5 5
10

3 3
2 2 2
1

6 1
1 6 1 2 0 4
11

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    count = 0

    if a[0] > x:
        count += a[0] - x
        a[0] -= count

    for i in range(n - 1):
        summed = a[i] + a[i + 1]

        if summed > x:
            diff = summed - x
            count += diff
            a[i + 1] -= diff

    print(count)
