# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    magic_count = 0
    slime_count = 1
    previous_slime = a[0]

    for i in range(1, n):
        if a[i] == previous_slime:
            slime_count += 1
        else:
            magic_count += slime_count // 2
            slime_count = 1

        previous_slime = a[i]

    print(magic_count + slime_count // 2)
