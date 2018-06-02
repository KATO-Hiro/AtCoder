'''input
4 2 3
1 4 2 3
2 3 2 3

3 1 10
3 3 4
3 3 4

1 3 3
3
3

'''

# -*- coding: utf-8 -*-

# SoundHound Inc. Programming Contest 2018 Spring
# Problem B

if __name__ == '__main__':
    n, l, r = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for i in range(len(a)):
        if a[i] < l:
            a[i] = l

        if a[i] > r:
            a[i] = r

    print(' '.join(map(str, list(a))))
