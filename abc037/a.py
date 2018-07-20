'''input
2 3 1
0

1 2 1
1

4 3 22
7

8 6 16
2

8 6 20
3

3 5 6
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))
    p, q = divmod(c, min(a, b))
    print(p)
