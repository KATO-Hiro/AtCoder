# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    ab = list()
    ans = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, bi))

    for aj, bj in sorted(ab, key=lambda x: x[0]):
        if m >= bj:
            ans += aj * bj
            m -= bj
        else:
            ans += aj * m
            break

    print(ans)


if __name__ == '__main__':
    main()
