# -*- coding: utf-8 -*-


def main():
    s = input().split("/")
    year = "".join(map(str, sorted(s[0])))
    month_day = "".join(map(str, sorted(s[1] + s[2])))

    if year == month_day:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
