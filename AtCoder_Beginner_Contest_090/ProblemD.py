'''input
5 2
7
10 0
100
31415 9265
287927211
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem D

if __name__ == '__main__':
    number, k = list(map(int, input().split()))
    count = 0

    # HACK: Not beautiful.
    if k == 0:
        print(number ** 2)
    else:
        for b in range(1, number + 1):
            p = (number + 1) // b
            r = number - (p * b)
            count += p * max(0, b - k)

            if (number + 1) % b != 0:
                count += max(0, r - k + 1)

        print(count)
