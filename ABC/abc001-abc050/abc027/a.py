'''input
5 5 5
5

1 1 2
2

4 3 4
3

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    from collections import Counter

    l = Counter(list(map(int, input().split())))

    for key, value in l.items():
        if value % 2 == 1:
            print(key)
            exit()
