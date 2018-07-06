'''input
4
ooxx
xoox
xxxx
xxxx

xxxo
xxoo
xxox
xxxx

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = int(input())
    s = [list(map(str, list(input()))) for _ in range(n)]
    mod_s = [[""] * n for _ in range(n)]

    for i in range(n):
        for j in range(n - 1, -1, -1):
            mod_s[i][j] = s[j][i]
            tmp_s = ''.join(map(str, mod_s[i]))
        print(tmp_s[::-1])
