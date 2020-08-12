# -*- coding: utf-8 -*-


def main():
    s = list(input())
    ans = 0

    for index, number in enumerate(s):
        if index % 2 == 0:
            ans += int(number)
        else:
            ans -= int(number)

    print(ans)


if __name__ == '__main__':
    main()
