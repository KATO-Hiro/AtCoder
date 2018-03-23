'''input
7 5 1
YES

2 2 1
NO

1 100 97
YES

40 98 58
YES

77 42 36
NO

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    count = 1

    while count < 10001:
        if ((a * count) % b) == c:
            print('YES')
            exit()

        count += 1

    print('NO')
