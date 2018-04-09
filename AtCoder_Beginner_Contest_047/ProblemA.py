'''input
30 30 100
No

10 30 20
Yes

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    candies = sorted(list(map(int, input().split())))

    first = sum(candies[:2])
    second = candies[2]

    if first == second:
        print('Yes')
    else:
        print('No')
