'''input
ggppgggpgg
2

gpg
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem D


if __name__ == '__main__':
    s = input()

    # See:
    # http://arc062.contest.atcoder.jp/data/arc/062/editorial.pdf
    print(len(s) // 2 - s.count('p'))
