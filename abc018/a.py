# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    result = [0, 0, 0]

    if a > b > c:
        result = [1, 2, 3]
    elif a > c > b:
        result = [1, 3, 2]
    elif b > a > c:
        result = [2, 1, 3]
    elif b > c > a:
        result = [3, 1, 2]
    elif c > a > b:
        result = [2, 3, 1]
    elif c > b > a:
        result = [3, 2, 1]

    for ans in result:
        print(ans)
