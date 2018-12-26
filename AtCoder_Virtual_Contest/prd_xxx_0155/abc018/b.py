# -*- coding: utf-8 -*-


def main():
    s = input()
    n = int(input())

    for i in range(n):
        li, ri = map(int, input().split())
        s = s[:li - 1] + s[li - 1:ri][::-1] + s[ri:]

    print(s)


if __name__ == '__main__':
    main()
