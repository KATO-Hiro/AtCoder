# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    s = input()

    if s[:a].isdigit() and s[a:a + 1] == '-' and s[a + 1:].isdigit():
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
