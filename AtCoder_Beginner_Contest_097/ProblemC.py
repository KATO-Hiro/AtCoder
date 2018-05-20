'''input
z
1
z

aba
4
b

atcoderandatcodeer
5
andat

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    s = input()
    k = int(input())
    extracted = set()
    s_len = len(s)

    # See:
    # https://beta.atcoder.jp/contests/abc097/submissions/2497319
    for i in range(1, min(k, s_len) + 1):
        for j in range(s_len - i + 1):
            extracted.add(s[j:i + j])

    print(sorted(extracted)[k - 1])
