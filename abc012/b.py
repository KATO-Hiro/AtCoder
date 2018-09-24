# -*- coding: utf-8 -*-


def main():
    n = int(input())
    hour = n // 3600
    minute = (n - 3600 * hour) // 60
    second = n - (3600 * hour) - (60 * minute)

    str_hour = str(hour)
    str_minute = str(minute)
    str_second = str(second)

    if len(str_hour) == 1:
        str_hour = '0' + str_hour
    if len(str_minute) == 1:
        str_minute = '0' + str_minute
    if len(str_second) == 1:
        str_second = '0' + str_second

    print(str_hour + ':' + str_minute + ':' + str_second)


if __name__ == '__main__':
    main()
