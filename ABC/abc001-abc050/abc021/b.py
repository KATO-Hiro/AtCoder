# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a, b = map(int, input().split())
    k = int(input())
    p = list(map(int, input().split()))
    p.append(a)
    p.append(b)

    if (k + 2) <= n and (k + 2 == len(set(p))):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
