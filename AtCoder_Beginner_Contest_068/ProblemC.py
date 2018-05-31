'''input
5 5
1 3
4 5
2 3
2 4
1 4
POSSIBLE

3 2
1 2
2 3
POSSIBLE

4 3
1 2
2 3
3 4
IMPOSSIBLE

100000 1
1 99999
IMPOSSIBLE

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    set_a = set()
    set_b = set()

    for i in range(m):
        a, b = list(map(int, input().split()))

        if a == 1:
            set_b.add(b)
        elif b == n:
            set_a.add(a)

    if len(set_a & set_b) > 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
