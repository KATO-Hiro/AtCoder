'''input
31415 92653
612
11009 11332
4
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    A, B = list(map(str, input().split()))

    count = 0

    for i in range(int(A), int(B) + 1):
        i = str(i)
        if (i[0] == i[4]) and (i[1] == i[3]):
            count += 1

    print(count)
