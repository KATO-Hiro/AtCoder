# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    ans = 0

    for i in range(1, n):
        ans = max(ans, len(set(s[:i]) & set(s[i:])))

    print(ans)


if __name__ == '__main__':
    main()
