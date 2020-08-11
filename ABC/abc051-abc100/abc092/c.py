'''input
6
-679 -2409 -3258 3095 -3291 -4462
21630
21630
19932
8924
21630
19288

3
3 5 -1
12
8
10

5
1 1 1 2 0
4
4
4
2
4

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    spot_count = int(input())
    spots = [0] + list(map(int, input().split())) + [0]

    # See:
    # https://www.youtube.com/watch?v=WFg2yJGZ2Cw
    # https://img.atcoder.jp/arc093/editorial.pdf
    total_distance = 0
    total_cost = 0

    for i in range(spot_count + 1):
        total_distance += abs(spots[i + 1] - spots[i])

    for j in range(1, spot_count + 1):
        shortcut_cost = (abs(spots[j - 1] - spots[j]) + abs(spots[j] - spots[j + 1]))
        total_cost = total_distance + abs(spots[j - 1] - spots[j + 1]) - shortcut_cost
        print(total_cost)
