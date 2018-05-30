'''input
WBWBWBWBWB
9

BBBWW
1

WWWWWW
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    s = input()
    count = 0

    # See:
    # https://beta.atcoder.jp/contests/abc047/submissions/1007244
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            count += 1

    print(count)
