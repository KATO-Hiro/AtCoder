'''input
5 20 100
7 17 120
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    N_hour, A, B = list(map(int, input().split()))

    result = min(N_hour * A, B)
    print(result)
