# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    ans = 0
    i = 0

    while i < n:
        if s[i:i + 2] == 'OX' or s[i:i + 2] == 'XO':
            i += 2
            ans += 1
        else:
            i += 1

    print(ans)


if __name__ == '__main__':
    main()
