'''input
4
2100 2500 2700 2700
2 2

5
1100 1900 2800 3200 3200
3 5

20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990
1 1

4
1100 1900 2799 4800
3 4

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    a = list(map(lambda x: int(x) // 400, input().split()))
    colors = [0] * 9

    # See:
    # https://beta.atcoder.jp/contests/abc064/submissions/2416018
    for i in a:
        if i < 8:
            colors[i] = 1
        else:
            colors[8] += 1

    kind = sum(colors[:8])
    print(max(kind, 1), kind + colors[8])
