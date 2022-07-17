# -*- coding: utf-8 -*-


def main():
    from datetime import date, timedelta
    import sys

    input = sys.stdin.readline

    s = input().rstrip().split("/")
    cur_day = date(*map(int, s))

    while True:
        formatted = cur_day.isoformat().replace("-", "/")

        if len(set(formatted)) <= 3:
            print(formatted)
            exit()

        cur_day += timedelta(days=1)


if __name__ == "__main__":
    main()
