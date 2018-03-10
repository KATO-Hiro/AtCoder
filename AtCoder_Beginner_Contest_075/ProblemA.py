'''input
5 7 5
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    A, B, C = list(map(int, input().split()))

    if A == B:
        print(C)
    elif B == C:
        print(A)
    else:
        print(B)
