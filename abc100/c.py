# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    for ai in a:
        while True:
            if ai % 2 == 0:
                ai = ai // 2
                count += 1
            else:
                break

    print(count)
