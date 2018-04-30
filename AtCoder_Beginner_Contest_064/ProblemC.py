'''input
4
2100 2500 2700 2700
2 2

5
1100 1900 2800 3200 3200
3 5

20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990
1 1

4
1100 1900 2799 4800
4 4

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    colors = [0] * 9
    rate = [1, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 4801]

    for ai in a:
        for k in range(9):
            if rate[k] <= ai < rate[k + 1]:
                colors[k] += 1
                break

    count = 0

    for i in range(7):
        if colors[i] > 0:
            count += 1

    red = colors[7]
    legend = colors[8]

    if (red == 0) and (legend == 0):
        print(count, count)
    elif (red > 0) and (legend == 0):
        print(count + 1, count + 1)
    elif (red == 0) and (legend > 0):
        print(count + 1, count + legend)
    else:
        print(count + 1, count + 1 + legend)
