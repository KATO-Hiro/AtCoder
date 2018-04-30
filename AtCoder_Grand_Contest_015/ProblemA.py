'''input
1000000000 1 1000000000
999999997000000003

3 3 4
2

4 4 6
5

5 4 3
0

1 7 10
0

1 3 3
1

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    n, a, b = list(map(int, input().split()))
    print(max((b - a) * (n - 2) + 1, 0))
