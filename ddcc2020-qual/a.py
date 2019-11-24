# -*- coding: utf-8 -*-


def main():
    x, y = map(int, input().split())
    ans = 0

    if x == 1:
        ans += 300000
    elif x == 2:
        ans += 200000
    elif x == 3:
        ans += 100000

    if y == 1:
        ans += 300000
    elif y == 2:
        ans += 200000
    elif y == 3:
        ans += 100000

    if x == 1 and y == 1:
        ans += 400000

    print(ans)


if __name__ == '__main__':
    main()
