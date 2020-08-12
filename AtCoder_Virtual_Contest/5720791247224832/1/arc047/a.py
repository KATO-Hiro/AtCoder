# -*- coding: utf-8 -*-


def main():
    n, l = map(int, input().split())
    s = input()
    ans = 0
    count = 1

    for si in s:
        if si == '+':
            count += 1
        else:
            count -= 1

        if count > l:
            ans += 1
            count = 1

    print(ans)


if __name__ == '__main__':
    main()
