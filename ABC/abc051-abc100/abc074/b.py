'''input
2
9
3 6
12

5
20
11 12 9 17 12
74
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    ball_count = int(input())
    robotB_position = int(input())
    positions = list(map(int, input().split()))

    total_length = 0

    for i in range(ball_count):
        if positions[i] < abs(robotB_position - positions[i]):
            total_length += 2 * positions[i]
        else:
            total_length += 2 * abs(robotB_position - positions[i])

    print(total_length)
