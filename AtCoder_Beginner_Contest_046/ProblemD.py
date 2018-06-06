'''input
ggppgggpgg
2

gpg
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem D


def execute_janken(self, other):
    if self == 'p' and other == 'g':
        return 1
    elif self == 'g' and other == 'p':
        return -1
    else:
        return 0


if __name__ == '__main__':
    s = input()
    p_count = 0
    g_count = 0
    score = 0
    hand = ''

    for si in s:
        if p_count == g_count:
            hand = 'g'
            g_count += 1
        elif p_count < g_count:
            hand = 'p'
            p_count += 1

        score += execute_janken(self=hand, other=si)

    print(score)
