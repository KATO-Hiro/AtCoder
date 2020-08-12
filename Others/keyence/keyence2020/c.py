# -*- coding: utf-8 -*-


def main():
    n, k, s = map(int, input().split())
    a = [0 for _ in range(n)]

    for i in range(n):
        if i < k:
            a[i] = s
        else:
            if s == 10 ** 9:
                a[i] = s - 1
            else:
                a[i] = s + 1

    print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()
