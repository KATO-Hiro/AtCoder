# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = input()
    val = 0
    ans = 0

    for si in s:
        if si == 'I':
            val += 1
        elif si == 'D':
            val -= 1

        ans = max(ans, val)

    print(ans)


if __name__ == '__main__':
    main()
