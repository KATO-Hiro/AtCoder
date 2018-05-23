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
    w_min, w_max = 0, w
    h_min, h_max = 0, h

    for _ in range(n):
        x, y, a = list(map(int, input().split()))

        if a == 1:
            w_min = max(x, w_min)
        elif a == 2:
            w_max = min(x, w_max)
        elif a == 3:
            h_min = max(y, h_min)
        elif a == 4:
            h_max = min(y, h_max)

    print(max(w_max - w_min, 0) * max(h_max - h_min, 0))
