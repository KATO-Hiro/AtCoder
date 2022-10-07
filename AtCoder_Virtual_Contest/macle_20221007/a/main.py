# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - days.index(s))


if __name__ == "__main__":
    main()
