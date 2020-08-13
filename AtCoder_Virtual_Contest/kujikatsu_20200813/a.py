# -*- coding: utf-8 -*-


def main():
    s = input()
    t = s[::-1]
    n = len(s) // 2
    count = 0

    for i in range(n):
        if s[i] != t[i]:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
