'''input
15
6

100000
10

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


if __name__ == '__main__':
    n = int(input())
    # See:
    # https://www.youtube.com/watch?v=Ommfmx2wtuY
    if (n == 10) or (n == 100) or (n == 1000) or (n == 10000) or (n == 100000):
        print(10)
    else:
        print(sum(list(map(int, list(str(n))))))
