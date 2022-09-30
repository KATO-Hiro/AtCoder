# -*- coding: utf-8 -*-


def main():
    from datetime import datetime, timedelta
    import sys

    input = sys.stdin.readline

    s_year, s_month, s_day = input().rstrip().split("-")
    t_year, t_month, t_day = input().rstrip().split("-")
    cur_day = datetime(int(s_year), int(s_month), int(s_day))
    end_day = datetime(int(t_year), int(t_month), int(t_day))
    one_day = timedelta(days=1)
    saturday = 5
    sunday = 6
    ans = 0

    while True:
        if cur_day.weekday() == saturday or cur_day.weekday() == sunday:
            ans += 1

        if cur_day == end_day:
            break

        cur_day += one_day

    print(ans)



if __name__ == "__main__":
    main()
