'''input
7 7 5
NO

5 5 7
YES

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    numbers = list(map(int, input().split()))

    if numbers.count(5) == 2 and numbers.count(7) == 1:
        print('YES')
    else:
        print('NO')
