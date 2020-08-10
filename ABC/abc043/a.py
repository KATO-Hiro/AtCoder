'''input
1
1

3
6

10
55

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    n = int(input())
    candy_count = 0

    for i in range(n + 1):
        candy_count += i

    print(candy_count)
