# -*- coding: utf-8 -*-


def main():
    b = list(map(str, input().split()))
    n = int(input())
    alpha = [str(i) for i in range(10)]
    d = dict()
    numbers = list()

    for bi, al in zip(b, alpha):
        d[bi] = al

    for i in range(n):
        a = input()
        s = ''

        for ai in a:
            s += d[ai]

        numbers.append((len(s), s, a))

    for j in sorted(numbers):
        print(j[2])


if __name__ == '__main__':
    main()
