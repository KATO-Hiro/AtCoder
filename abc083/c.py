'''input
1 3
2

314159265 358979323846264338
31

3 20
3

25 100
3

1 1
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    x, y = map(int, input().split())
    count = 0

    while x * (2 ** count) <= y:
        count += 1

    print(count)
