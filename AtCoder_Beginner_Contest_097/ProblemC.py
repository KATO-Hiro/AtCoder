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
    extracted = list()
    s_len = len(s)

    for i in range(1, min(k, s_len) + 1):
        start = 0
        ended = i

        for j in range(s_len - i + 1):
            sub_str = s[start:ended]

            if sub_str not in extracted:
                extracted.append(sub_str)

            start += 1
            ended += 1

    sorted_extracted = sorted(extracted)
    print(sorted_extracted[k - 1])
