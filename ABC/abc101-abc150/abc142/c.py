# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    ans = list()

    for i, ai in enumerate(a, 1):
        d[i] = ai

    for j, di in sorted(d.items(), key=lambda x: x[1]):
        ans.append(j)

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
