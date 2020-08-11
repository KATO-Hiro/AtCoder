# -*- coding: utf-8 -*-


def main():
    s = input()
    ans = 0

    for a, b in zip(s, s[::-1]):
        if a != b:
            ans += 1

    print(ans // 2)


if __name__ == '__main__':
    main()
