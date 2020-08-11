# -*- coding: utf-8 -*-


def main():
    k = int(input())
    n = 50
    p, q = divmod(k, n)
    a = [i + p for i in range(n)]

    for i in range(q):
        for j in range(n):
            if j == i:
                a[j] += 50
            else:
                a[j] -= 1

    print(n)
    print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()
