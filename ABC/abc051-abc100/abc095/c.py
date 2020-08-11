'''input
1500 2000 500 90000 100000
100000000

1500 2000 1600 3 2
7900

1500 2000 1900 3 2
8500

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    a, b, c, x, y = list(map(int, input().split()))
    ab_yen = a + b
    c_yen = 2 * c
    min_x_y_count = min(x, y)
    cost = 0

    if ab_yen >= c_yen:
        cost += c_yen * min_x_y_count
        cost += min(a, c_yen) * (x - min_x_y_count)
        cost += min(b, c_yen) * (y - min_x_y_count)
    else:
        cost = (a * x) + (b * y)

    print(cost)
