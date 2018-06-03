'''input
2
1 1000000000
1000000000 1
1000000001

3
4 7
2 9
6 2
8

5
1 10
3 6
5 2
4 4
2 8
7

'''

# -*- coding: utf-8 -*-

# Tenka1 Programmer Beginner Contest
# Problem B

if __name__ == '__main__':
    n = int(input())
    worst_rank = -1
    worst_score = float('inf')

    # See:
    # https://beta.atcoder.jp/contests/tenka1-2017-beginner/submissions/1637273
    for i in range(n):
        ai, bi = list(map(int, input().split()))
        worst_rank = max(worst_rank, ai)
        worst_score = min(worst_score, bi)

    print(worst_rank + worst_score)
