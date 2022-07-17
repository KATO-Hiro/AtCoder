# -*- coding: utf-8 -*-


def get_day(day):
    return str(day).replace("-", "/").replace(" 00:00:00", "")


def main():
    from datetime import datetime, timedelta
    import sys

    input = sys.stdin.readline

    s = input().rstrip().split("/")
    start_day = datetime(int(s[0]), int(s[1]), int(s[2]))
    one_day = timedelta(days=1)
    next_day = start_day

    while True:
        candidate = get_day(next_day)

        if len(set(list(candidate))) <= 3:
            print(candidate)
            exit()

        next_day += one_day


if __name__ == "__main__":
    main()
