'''input
10 10 5
1 6 1
4 1 3
6 9 4
9 4 2
3 1 3
64

5 4 2
2 1 1
3 3 4
9

5 4 3
2 1 1
3 3 4
1 4 2
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    w, h, n = list(map(int, input().split()))
    xya = [list(map(int, input().split())) for _ in range(n)]
    w_min = 0
    w_max = w
    h_min = 0
    h_max = h

    for x, y, a in xya:
        if (a == 1) and (x > w_min):
            w_min = x
        elif (a == 2) and (x < w_max):
            w_max = x
        elif (a == 3) and (y > h_min):
            h_min = y
        elif (a == 4) and (y < h_max):
            h_max = y

    print(max(w_max - w_min, 0) * max(h_max - h_min, 0))
