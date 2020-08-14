# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    c = [[0 for _ in range(w)] for __ in range(h)]
    k = 0

    for j in range(h):
        if j % 2 == 0:
            for i in range(w):
                c[j][i] = k + 1
                a[k] -= 1

                if a[k] == 0:
                    k += 1
        else:
            for i in range(w - 1, -1, -1):
                c[j][i] = k + 1
                a[k] -= 1

                if a[k] == 0:
                    k += 1

    for ci in c:
        print(' '.join(map(str, ci)))


if __name__ == '__main__':
    main()
