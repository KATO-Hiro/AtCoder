# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    total = 0

    for i in range(3):
        s, e = list(map(int, input().split()))
        total += int(s * e // 10)

    print(total)
