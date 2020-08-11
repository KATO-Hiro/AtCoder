# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    magic_count = 0
    previous_slime = a[0]

    # See:
    # https://beta.atcoder.jp/contests/agc026/submissions/2841276
    for i in range(1, n):
        if a[i] == previous_slime:
            magic_count += 1
            previous_slime = -1
        else:
            previous_slime = a[i]

    print(magic_count)
