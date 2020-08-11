'''input
10 90 20 80
60

0 33 66 99
0

0 75 25 100
50

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    times = list(map(int, input().split()))

    alice_start = times[0]
    alice_end = times[1]
    bob_start = times[2]
    bob_end = times[3]

    if (bob_end < alice_start) or (alice_end < bob_start):
        print(0)
    else:
        sorted_times = sorted(times)
        print(sorted_times[2] - sorted_times[1])
