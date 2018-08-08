# -*- coding: utf-8 -*-


def main():
    n, l = list(map(int, input().split()))
    s = input()
    tab_count = 1
    crash_count = 0

    for si in s:
        if si == '+':
            tab_count += 1
        else:
            tab_count -= 1

        if tab_count > l:
            crash_count += 1
            tab_count = 1

    print(crash_count)


if __name__ == '__main__':
    main()
