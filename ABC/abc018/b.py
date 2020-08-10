# -*- coding: utf-8 -*-


def main():
    s = input()
    n = int(input())

    for i in range(n):
        left, right = map(int, input().split())
        partly_s = s[left - 1:right]
        s = s[:left - 1] + partly_s[::-1] + s[right:]

    print(s)


if __name__ == '__main__':
    main()
