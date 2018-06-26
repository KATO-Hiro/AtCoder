'''input
1
0

100000
37

26
1

41
4

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    n = int(input())
    diff = 0
    mod = 0
    total_sum = float('inf')

    if n == 1:
        print(0)
    else:
        for i in range(1, n):
            p, q = divmod(n, i)

            total_sum = min(total_sum, abs(p - i) + q)

        print(total_sum)
