# -*- coding: utf-8 -*-


def main():
    n, h, w = map(int, input().split())
    ans = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        ans += min(ai // h, bi // w)

    print(ans)


if __name__ == '__main__':
    main()
