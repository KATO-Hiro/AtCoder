# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        ans = max(ans, ai + bi)

    print(ans)


if __name__ == '__main__':
    main()
