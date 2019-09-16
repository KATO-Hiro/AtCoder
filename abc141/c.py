# -*- coding: utf-8 -*-


def main():
    n, k, q = map(int, input().split())
    ac = [0 for _ in range(n)]

    for i in range(q):
        ai = int(input()) - 1
        ac[ai] += 1

    for j in ac:
        if k + j - q > 0:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
