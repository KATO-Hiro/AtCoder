'''input
999999999 999999999 999999999
999999998000000001

1000000000 999999999 999999999
0

6 3 5
0

7 3 5
15

5 3 5
15

3 3 3
9

2 2 4
0

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    numbers = sorted(list(map(int, input().split())))

    if numbers[2] % 2 == 0:
        print(0)
    else:
        print(numbers[0] * numbers[1])
