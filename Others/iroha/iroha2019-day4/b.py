# -*- coding: utf-8 -*-


def main():
    n, m, l = map(int, input().split())
    ans = m * l

    for i in range(n):
        ai, bi = map(int, input().split())
        ans = min(ans, ai + bi * m)

    print(ans)


if __name__ == '__main__':
    main()
