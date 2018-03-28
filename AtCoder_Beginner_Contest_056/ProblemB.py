'''input
3 1 3
0

5 10 1
4

3 2 6
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    width, a, b = list(map(int, input().split()))

    if (a + width) < b:
        print(min(b - (a + width), b - a))
    elif a <= b <= (a + width):
        print(0)
    else:
        print(min(a - b, a - (b + width)))
