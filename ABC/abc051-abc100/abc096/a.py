'''input
2 1
1

12 5
11

11 30
11

5 5
5

'''

# -*- coding: utf-8 -*-

# atcoder beginner contest
# problem a

if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    if a <= b:
        print(a)
    else:
        print(a - 1)
