# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t_count = s.count("T")
    a_count = s.count("A")

    if t_count > a_count:
        print("T")
    elif t_count < a_count:
        print("A")
    else:
        t_max = 0
        a_max = 0

        for i, si in enumerate(s):
            if si == "T":
                t_max = i
            else:
                a_max = i

        if t_max < a_max:
            print("T")
        else:
            print("A")


if __name__ == "__main__":
    main()
