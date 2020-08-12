'''input
5 314
10101
159
265
358
979
323
2031

3 5
011
8
10
3
16

'''

# -*- coding: utf-8 -*-

# COLOCON Colopl programming contest 2018 qual A
# Problem B

if __name__ == '__main__':
    n, x = list(map(int, input().split()))
    s = input()
    ts = [int(input()) for _ in range(n)]
    total_time = 0

    for i in range(len(s)):
        if s[i] == '0':
            total_time += ts[i]
        else:
            total_time += min(ts[i], x)

    print(total_time)
