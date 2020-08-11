# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s, t = input().split()
    ans = ''

    for si, ti in zip(s, t):
        ans += si
        ans += ti

    print(ans)


if __name__ == '__main__':
    main()
