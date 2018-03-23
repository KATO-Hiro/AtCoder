'''input
yakiniku unagi sushi
NO

rng gorilla apple
YES

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    a, b, c = input().split()

    if (a[-1] == b[0]) and (b[-1] == c[0]):
        print('YES')
    else:
        print('NO')
