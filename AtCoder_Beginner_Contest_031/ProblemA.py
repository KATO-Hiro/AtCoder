'''input
3 3
12

31 87
2784

101 65
6666

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, d = list(map(int, input().split()))

    if a <= d:
        print((a + 1) * d)
    else:
        print(a * (d + 1))
