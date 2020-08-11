# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    ans = 0
    empty = 1

    for i in range(20 + 1):
        if empty >= b:
            print(max(0, ans - 1))
            exit()
        else:
            ans += 1
            empty = i * a - ((i - 1))


if __name__ == '__main__':
    main()
