'''input
5 10
0 3 5 7 100
17
27

4 10
0 3 5 7
17

9 10
0 3 5 7 100 110 200 300 311
67

2 4
0 3
7

2 4
0 5
8

4 1000000000
0 1000 1000000 1000000000
2000000000

1 1
0
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n, intervel = list(map(int, input().split()))
    ts = list(map(int, input().split()))
    ts += [ts[-1] + intervel]

    total_t = 0
    previous_t = ts[0]

    for i in range(1, n + 1):
        current_t = ts[i]

        if (previous_t + intervel) > current_t:
            total_t += max(0, current_t - previous_t)
        else:
            total_t += intervel

        previous_t = current_t

    print(total_t)
