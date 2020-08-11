'''input
45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir
9

6
aabbca
2

10
aaaaaaaaaa
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = 0

    for i in range(1, len(s)):
        tmp = set(s[:i]) & set(s[i:])
        result = max(len(tmp), result)

    print(result)
