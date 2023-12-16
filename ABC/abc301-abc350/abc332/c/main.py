# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = input().rstrip()
    remain_m = m
    logo = 0
    remain_logo = 0

    for si in s:
        if si == "0":
            remain_m = m
            remain_logo = logo
        elif si == "1":
            if remain_m >= 1:
                remain_m -= 1
            else:
                if remain_logo >= 1:
                    remain_logo -= 1
                else:
                    logo += 1
        elif si == "2":
            if remain_logo >= 1:
                remain_logo -= 1
            else:
                logo += 1

    print(logo)


if __name__ == "__main__":
    main()
