# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(abs(max(a) - min(a)))
