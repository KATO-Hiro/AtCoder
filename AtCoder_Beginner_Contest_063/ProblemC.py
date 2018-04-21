'''input
3
15
10
25
35

3
5
10
15
25

3
10
20
30
0

3
10
10
15
35

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    s = sorted([int(input()) for _ in range(n)])
    score_max = sum(s)

    if score_max % 10 == 0:
        candidates = [si for si in s if si % 10 != 0]

        if len(candidates) == 0:
            score_max = 0
        else:
            score_max -= min(candidates)

    print(score_max)
