# -*- coding: utf-8 -*-


def main():
    s = input()
    k = int(input())
    n = len(s)
    q = k % n

    print(s[q:] + s[:q])


if __name__ == '__main__':
    main()
