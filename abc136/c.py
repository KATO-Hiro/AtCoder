# -*- coding: utf-8 -*-


def main():
    n = int(input())
    h = list(map(int, input().split()))

    if n == 1:
        print('Yes')
        exit()

    for i in range(n - 1, 0, -1):
        if h[i] >= h[i - 1]:
            continue
        else:
            if h[i] - h[i - 1] == -1:
                h[i - 1] -= 1
            else:
                print('No')
                exit()

    print('Yes')


if __name__ == '__main__':
    main()
