'''input
6
382253568 723152896 37802240 379425024 404894720 471526144
8

4
5 6 8 10
0

3
8 12 40
2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B


def is_even(a):
    result = [a[x] % 2 for x in range(len(a))]
    if sum(result) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    number = int(input())
    a = list(map(int, input().split()))
    count = 0

    while is_even(a):
        a = [int(a[x] / 2) for x in range(number)]
        count += 1

    print(count)
