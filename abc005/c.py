# -*- coding: utf-8 -*-


def main():
    t = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    count = 0
    i = 0
    j = 0

    while i < n:
        if j >= m:
            break

        if a[i] <= b[j] <= a[i] + t:
            j += 1
            count += 1

        i += 1

    if count >= m:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
