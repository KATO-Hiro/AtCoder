# -*- coding: utf-8 -*-


def main():
    n, q = map(int, input().split())
    s = input()
    m = len(s)
    ac = [0 for _ in range(m)]

    for k in range(m - 1):
        if s[k] == 'A' and s[k + 1] == 'C':
            ac[k + 1] = ac[k] + 1
        else:
            ac[k + 1] = ac[k]

    for i in range(q):
        li, ri = map(int, input().split())
        print(ac[ri - 1] - ac[li - 1])


if __name__ == '__main__':
    main()
