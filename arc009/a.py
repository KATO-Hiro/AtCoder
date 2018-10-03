# -*- coding: utf-8 -*-


def main():
    n = int(input())
    ans = 0

    for i in range(n):
        ai, bi = map(int, input().split())
        ans += ai * bi * 1.05

    print(int(ans))


if __name__ == '__main__':
    main()
